from ai_model.knowledge_model import KnowledgeModel
from config import MIN_SIMILARITY, KNOWLEDGE_JSON_PATH

knowledge = KnowledgeModel(KNOWLEDGE_JSON_PATH, MIN_SIMILARITY)