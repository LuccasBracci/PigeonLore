{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNSI5sD27UYO/EDVnTy53uU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/PigeonLore/PigeonLore/blob/main/ReadnPorts.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3Nfia0GoYuS4",
        "outputId": "32771670-8145-4a27-c65b-82c158bf088e"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "'''\n",
        " Just imports dependancies in one package \n",
        "'''\n",
        "\n",
        "import numpy as np\n",
        "import pandas as pd\n",
        "from google.colab import drive\n",
        "from sklearn.impute import SimpleImputer\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
        "from sklearn.compose import make_column_selector, make_column_transformer\n",
        "\n",
        "drive.mount('/content/drive')\n",
        "\n",
        "def dfRead(filepath):\n",
        "  global df \n",
        "  df = pd.read_csv(filepath)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "dfRead()"
      ],
      "metadata": {
        "id": "N8RHnxeKZr2Z"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}