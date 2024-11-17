from sentence_transformers import SentenceTransformer, util
import os

from dto.similar_dto import similar_dto
from config import MODEL_FOLDER_PATH, MODEL_NAME

class SentenceSimilar:
    def __init__(self):
        self.model_absolute_path = os.getcwd() + MODEL_FOLDER_PATH

        self.model = None

        if not self._is_model_local_exist():
            if not os.path.exists(self.model_absolute_path):
                os.makedirs(self.model_absolute_path)

            self.model = SentenceTransformer(MODEL_NAME)
            self.model.save(self.model_absolute_path)
            return

        self.model = SentenceTransformer(self.model_absolute_path)


    
    def check(self, input, questions):
        input_embedding = self.model.encode(input)
        question_embeddings = self.model.encode(questions)

        similarities = util.pytorch_cos_sim(input_embedding, question_embeddings)
        most_similar_question_idx = similarities.argmax()
        most_similar_question = questions[most_similar_question_idx]
        similarity_score = similarities[0][most_similar_question_idx].item()

        return similar_dto(most_similar_question_idx, most_similar_question, similarity_score)

    def check_all(self, input, questions):
        input_embedding = self.model.encode(input)
        question_embeddings = self.model.encode(questions)

        similarities = util.pytorch_cos_sim(input_embedding, question_embeddings)

        similarities_list = similarities[0].tolist()

        result = list(map(lambda x: similar_dto(x[0], x[1], similarities_list[x[0]]), enumerate(questions)))

        return result



    def _is_model_local_exist(self):
        required_files = [
            'config.json',
            'config_sentence_transformers.json',
            'model.safetensors',
            'modules.json',
            'sentence_bert_config.json',
            'special_tokens_map.json',
            'tokenizer.json',
            'tokenizer_config.json',
            'unigram.json'
        ]

        for file_name in required_files:
            file_path = os.path.join(self.model_absolute_path, file_name)
            if not os.path.isfile(file_path):
                return False
        return True

