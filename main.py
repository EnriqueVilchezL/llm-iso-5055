def main():
    import logging
    import os
    from dotenv import load_dotenv
    from langchain_google_genai import ChatGoogleGenerativeAI

    from github_fetch import GitHubRepositoryFetcher
    from llm import LLM
    from zip_processor import ZipFileProcessor

    # Load environment variables from .env file
    load_dotenv()

    # Set up logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # zip_processor = ZipFileProcessor(
    #     zip_file_path="ai_workshop_2025_neural_networks_math-main.zip",
    #     logger=logger,
    # )
    # files = zip_processor.get_all_files(
    #     allowed_extensions=[".py"],
    #     verbose=True,
    # )

    llm = LLM(
        model=ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            google_api_key=os.getenv("API_KEY"),
        )
    )
    print(llm.generate("Hello, world!"))

    # for file in files:
    #     print(file)


if __name__ == "__main__":
    main()
