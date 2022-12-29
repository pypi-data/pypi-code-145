"""Wrapper around NLPCloud APIs."""
from typing import Any, Dict, List, Mapping, Optional

from pydantic import BaseModel, Extra, root_validator

from langchain.llms.base import LLM
from langchain.utils import get_from_dict_or_env


class NLPCloud(LLM, BaseModel):
    """Wrapper around NLPCloud large language models.

    To use, you should have the ``nlpcloud`` python package installed, and the
    environment variable ``NLPCLOUD_API_KEY`` set with your API key.

    Example:
        .. code-block:: python

            from langchain import NLPCloud
            nlpcloud = NLPCloud(model="gpt-neox-20b")
    """

    client: Any  #: :meta private:
    model_name: str = "finetuned-gpt-neox-20b"
    """Model name to use."""
    temperature: float = 0.7
    """What sampling temperature to use."""
    min_length: int = 1
    """The minimum number of tokens to generate in the completion."""
    max_length: int = 256
    """The maximum number of tokens to generate in the completion."""
    length_no_input: bool = True
    """Whether min_length and max_length should include the length of the input."""
    remove_input: bool = True
    """Remove input text from API response"""
    remove_end_sequence: bool = True
    """Whether or not to remove the end sequence token."""
    bad_words: List[str] = []
    """List of tokens not allowed to be generated."""
    top_p: int = 1
    """Total probability mass of tokens to consider at each step."""
    top_k: int = 50
    """The number of highest probability tokens to keep for top-k filtering."""
    repetition_penalty: float = 1.0
    """Penalizes repeated tokens. 1.0 means no penalty."""
    length_penalty: float = 1.0
    """Exponential penalty to the length."""
    do_sample: bool = True
    """Whether to use sampling (True) or greedy decoding."""
    num_beams: int = 1
    """Number of beams for beam search."""
    early_stopping: bool = False
    """Whether to stop beam search at num_beams sentences."""
    num_return_sequences: int = 1
    """How many completions to generate for each prompt."""

    nlpcloud_api_key: Optional[str] = None

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    @root_validator()
    def validate_environment(cls, values: Dict) -> Dict:
        """Validate that api key and python package exists in environment."""
        nlpcloud_api_key = get_from_dict_or_env(
            values, "nlpcloud_api_key", "NLPCLOUD_API_KEY"
        )
        try:
            import nlpcloud

            values["client"] = nlpcloud.Client(
                values["model_name"], nlpcloud_api_key, gpu=True, lang="en"
            )
        except ImportError:
            raise ValueError(
                "Could not import nlpcloud python package. "
                "Please it install it with `pip install nlpcloud`."
            )
        return values

    @property
    def _default_params(self) -> Mapping[str, Any]:
        """Get the default parameters for calling NLPCloud API."""
        return {
            "temperature": self.temperature,
            "min_length": self.min_length,
            "max_length": self.max_length,
            "length_no_input": self.length_no_input,
            "remove_input": self.remove_input,
            "remove_end_sequence": self.remove_end_sequence,
            "bad_words": self.bad_words,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "repetition_penalty": self.repetition_penalty,
            "length_penalty": self.length_penalty,
            "do_sample": self.do_sample,
            "num_beams": self.num_beams,
            "early_stopping": self.early_stopping,
            "num_return_sequences": self.num_return_sequences,
        }

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {**{"model_name": self.model_name}, **self._default_params}

    @property
    def _llm_type(self) -> str:
        """Return type of llm."""
        return "nlpcloud"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        """Call out to NLPCloud's create endpoint.

        Args:
            prompt: The prompt to pass into the model.
            stop: Not supported by this interface (pass in init method)

        Returns:
            The string generated by the model.

        Example:
            .. code-block:: python

                response = nlpcloud("Tell me a joke.")
        """
        if stop and len(stop) > 1:
            raise ValueError(
                "NLPCloud only supports a single stop sequence per generation."
                "Pass in a list of length 1."
            )
        elif stop and len(stop) == 1:
            end_sequence = stop[0]
        else:
            end_sequence = None
        response = self.client.generation(
            prompt, end_sequence=end_sequence, **self._default_params
        )
        return response["generated_text"]
