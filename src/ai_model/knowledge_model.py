from ai_model.sentence_similar import SentenceSimilar
import json

class KnowledgeModel(SentenceSimilar):
    def __init__(self, knowledge_path, min_similarity):
        super().__init__()
        self.knowledge_path = knowledge_path
        self.min_similarity = min_similarity
        self.update()
        
    def update(self):
        with open(self.knowledge_path, 'r', encoding='utf-8') as file:
            self.knowledge_data = json.load(file)

    def get_knowledge_questions(self, only_first_question=False):
        all_questions = []

        if only_first_question:
            for item in self.knowledge_data['knowledge']:
                all_questions.append(item['questions'][0])
            return all_questions

        for item in self.knowledge_data['knowledge']:
            all_questions.extend(item['questions'])

        return all_questions
    
    def find_answer(self, similar_question):
        for item in self.knowledge_data['knowledge']:
            for q in item['questions']:
                if q == similar_question:
                    return item['answer']
        raise ValueError()

    def find_question_id(self, similar_question):
        for index, item in enumerate(self.knowledge_data['knowledge']):
            for q in item['questions']:
                if q == similar_question:
                    return index
        raise ValueError("Question not found")

    def get_answer_by_id(self, id):
        question_data = self.get_question_data_by_id(id)
        return question_data['answer']

    def get_question_by_id(self, id):
        question_data = self.get_question_data_by_id(id)
        return question_data['questions'][0]

    def get_question_data_by_id(self, id):
        if len(self.knowledge_data['knowledge']) -1 < id:
            raise ValueError()
        return self.knowledge_data['knowledge'][id]
    
    def get_answer(self, question):
        questions = self.get_knowledge_questions()
        similar_question_data = super().check(question, questions)

        if similar_question_data.probability <= self.min_similarity:
            raise ValueError()
        
        answer = self.find_answer(similar_question_data.text)
        return answer

    def get_similar_questions(self, question):
        questions = self.get_knowledge_questions()
        similar_questions_data = super().check_all(question, questions)
        return sorted(similar_questions_data, key=lambda obj: obj.probability, reverse=True)




