# Wearable Voice Assistant

## Overview
Wearable Voice Assistant is a project aimed at assisting visually impaired individuals by providing them with a voice-based interface to interact with technology. This project utilizes OpenAI's GPT-3.5 language model to answer questions and communicate with the user, as well as integrating image description capabilities using images captured by ESP32-CAM.

## Features
- Voice-based interaction: Users can ask questions and receive responses through voice commands.
- Access to GPT-3.5: Utilizes OpenAI's GPT-3.5 model to provide accurate and informative responses.
- Image description: Ability to capture images using ESP32-CAM and receive verbal descriptions of the images.
- Accessibility: Designed specifically for visually impaired individuals to improve their interaction with technology.

## Installation
1. Clone the repository: `git clone https://github.com/yourusername/wearable-voice-assistant.git`
2. Install required dependencies: pip install openai python-dotenv speechrecognition pyttsx3 numpy pyaudio
3. Set up ESP32-CAM:
- Follow instructions provided by the ESP32-CAM documentation to configure and connect the camera module.
4. Obtain GPT-3.5 API key:
- Visit the OpenAI website to obtain an API key for accessing the GPT-3.5 model.
5. Configure API key:
- Add your OpenAI API key to the appropriate configuration file or environment variable.


## Contribution
Contributions to the Wearable Voice Assistant project are welcome. If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/improvement`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/improvement`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements
- OpenAI for providing access to the GPT-3.5 model.
- Espressif Systems for developing the ESP32-CAM module.
- Contributors to the project.

## Contact
For any inquiries or support regarding the Wearable Voice Assistant project, feel free to contact us at example@email.com.
