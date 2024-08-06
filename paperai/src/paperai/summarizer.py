from transformers import pipeline

class Summarizer:
    def __init__(self, model_name='sshleifer/distilbart-cnn-12-6'):
        self.summarizer = pipeline('summarization', model=model_name)

    def summarize(self, text, max_length=130, min_length=30, do_sample=False):
        """Summarizes the given text using the pre-trained model.

        Args:
            text (str): The text to be summarized.
            max_length (int): The maximum length of the summary.
            min_length (int): The minimum length of the summary.
            do_sample (bool): Whether to use sampling for generating the summary.

        Returns:
            str: The summarized text.
        """
        summary = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)
        return summary[0]['summary_text']

if __name__ == '__main__':
    # Example usage
    text = """The US Department of Justice is conducting a criminal investigation into Boeing. The investigation is focused on the 737 Max jet. The 737 Max has been involved in two fatal crashes. The crashes killed 346 people. The Justice Department is investigating whether Boeing misled regulators about the safety of the 737 Max."""
    summarizer = Summarizer()
    summary = summarizer.summarize(text)
    print(summary)