 f-ANIME - Anime Snapping Tool

f-ANIME is a Streamlit web application that allows users to upload anime cutscenes and get information about the anime, including its description, availability, episode list, and manga availability.

## Features

- Upload any cutscenes of anime.
- Find information about the anime.
- Find links to watch the anime.
- Get the episode list of the anime.
- Find the manga availability.

## How to Use

1. Visit the [f-ANIME web app](https://example.com) (deployment under process).
2. Upload an image of the anime cutscene.
3. Choose an action from the available buttons:
   - **Tell me about the anime**: Provides information about the anime.
   - **Find the link**: Finds links to watch the anime.
   - **Episode list**: Retrieves the episode list of the anime.
   - **Manga finder**: Finds the manga availability.
4. View the response provided by the app.

## Requirements

- Python 3.6+
- Streamlit
- Pillow
- google-generativeai (Gemini API wrapper)
- dotenv

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/bineetbairagi/f-ANIME.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## Configuration

- Set up a `.env` file with the following content:

  ```plaintext
  Gemini_Api_Key="AIzaSyCv3WHh-Drrqdi_HhIZCAPLRaqvrViePiI"
  ```


## Author

- [RAIDEN](https://www.linkedin.com/in/bineet-bairagi-a046112a2/)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README file according to your project's specifics, including installation instructions, usage guidelines, and any other relevant information.
