from langchain_community.llms import BaseLLM


class LLM:
    def __init__(self, model: BaseLLM):
        """
        Initialize the LLM with a model.
        :param model: LLM, the model to use for text generation
        """
        self.model = model

    def generate(self, prompt: str) -> str:
        """
        Generate text using the model.
        :param prompt: str, the input prompt for text generation
        :return: str, the generated text
        """
        return self.model.invoke(prompt).content
