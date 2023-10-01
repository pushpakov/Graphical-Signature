# Graphical Signature Generator

This Python script allows you to create a graphical signature with your name using the Python Imaging Library (PIL). Follow the steps below to generate your signature.

## Getting Started

### Prerequisites

- Python: Ensure you have Python installed on your computer. You can download it from the official Python website [here](https://www.python.org/downloads/).

- Pillow Library: You'll need the Pillow library for image processing. Install it using pip:

  ```bash
  pip install Pillow

## Usage

1. **Clone the Repository**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/pushpakov/Graphical-Signature.git
   cd graphical-signature-generator

2. **Run the Script:**

   Execute the Python script to generate your graphical signature. You'll be prompted to enter your name:

   ```bash
   python generate_signature.py

3. **View Your Signature:**

    After running the script, your graphical signature will be saved as "signature.png" in the same directory. You can view it or use it as needed.

## Customization

### Font
You can customize the font used for your signature by replacing the `"Alivia.otf"` font file with any TTF or OTF font file of your choice. Make sure to provide the correct path to the font file.

### Font Size
Adjust the `font_size` variable in the script to change the size of the signature font.

## Example

Here's an example of how the script works:

```bash
python generate_signature.py
```
Running the script will prompt you to enter your name for generating the graphical signature. For example:
```bash
Enter your name for generating graphical signature: Pushpak Kumar # you can enter any name here for which you want to generate the graphical signature.
```
The generated graphical signature will get saved in the path mentioned in the script:

![Graphical Signature](signature.png)
