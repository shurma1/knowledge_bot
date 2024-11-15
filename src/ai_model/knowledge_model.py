from ai_model.sentence_similar import SentenceSimilar
import json

class KnowledgeModel(SentenceSimilar):
    def __init__(self, knowledge_path, min_similarity):
        super().__init__()
        self.knowledge_path = knowledge_path
        self.min_similarity = min_similarity
        self.update()
        
    def update(self):
        print(self.knowledge_path)
        with open(self.knowledge_path, 'r', encoding='utf-8') as file:
            self.knowledge_data = json.load(file)

    def _get_knowledge_questions(self):
        all_questions = []
        for item in self.knowledge_data['knowledge']:
            all_questions.extend(item['questions'])

        return all_questions
    
    def _find_answer(self, similar_question):
        for item in self.knowledge_data['knowledge']:
            for q in item['questions']:
                if q == similar_question:
                    return item['answer']
        raise ValueError()
    
    def get_answer(self, question):
        questions = self._get_knowledge_questions()
        similar_question_data = super().check(question, questions)

        if similar_question_data.probability <= self.min_similarity:
            raise ValueError()
        
        answer = self._find_answer(similar_question_data.text)
        return answer


