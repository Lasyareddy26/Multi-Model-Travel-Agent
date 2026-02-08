from litellm.router import Router
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage
from langchain_core.outputs import ChatResult, ChatGeneration
from pydantic import Field
from typing import Any, List, Optional
from config import Config

def init_router():
    model_list = []
    for key in Config.GEMINI_KEYS:
        model_list.append({
            "model_name": "smart-tier",
            "litellm_params": {"model": Config.SMART_MODELS[0], "api_key": key}
        })
    for key in Config.GROQ_KEYS:
        model_list.append({
            "model_name": "fast-tier",
            "litellm_params": {"model": Config.FAST_MODELS[0], "api_key": key}
        })
    # num_retries=3 helps handle temporary rate limit spikes automatically
    return Router(model_list=model_list, routing_strategy="simple-shuffle", num_retries=3)

class TravelLLM(BaseChatModel):
    router: Any = Field(...)
    group: str = Field(...)
    
    def _generate(self, messages: List[Any], stop: Optional[List[str]] = None) -> ChatResult:
        formatted = [{"role": "user", "content": m.content} for m in messages]
        response = self.router.completion(model=self.group, messages=formatted)
        content = response.choices[0].message.content
        
        # FIXED: Returning official LangChain objects prevents the 'generation_info' error
        generation = ChatGeneration(
            message=AIMessage(content=content),
            generation_info={"model_name": response.model}
        )
        return ChatResult(generations=[generation])

    @property
    def _llm_type(self) -> str: return "travel_hybrid_agent"