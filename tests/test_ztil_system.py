{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPvU+zEvD5RNwsHogMAS95e",
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
        "<a href=\"https://colab.research.google.com/github/jannikm81-gif/Humanitas-purissima-/blob/main/tests/test_ztil_system.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "75V_4tYrtpcd"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "\n",
        "def berechne_ztil_end_utility(staats_angriff, angriffs_zeitpunkt, sperr_haerte):\n",
        "    \"\"\"Numerische Hilfsfunktion zur Abbildung der ZTIL-Kerninvariante.\"\"\"\n",
        "    zeit = np.linspace(0, 200, 200)\n",
        "    staats_kollektiv = np.ones(200) * 100.0\n",
        "\n",
        "    if staats_angriff:\n",
        "        for i, t in enumerate(zeit):\n",
        "            if t >= angriffs_zeitpunkt:\n",
        "                dt = t - angriffs_zeitpunkt\n",
        "                staats_kollektiv[i] = max(0, 100.0 - dt * (sperr_haerte * 0.8))\n",
        "    return staats_kollektiv[-1]\n",
        "\n",
        "def test_ztil_isolation_kollaps():\n",
        "    \"\"\"Überprüft, ob das kollektive Sub-Grid bei maximaler Sperrhärte gegen Null gedrückt wird.\"\"\"\n",
        "    end_utility = berechne_ztil_end_utility(staats_angriff=True, angriffs_zeitpunkt=50, sperr_haerte=10.0)\n",
        "    assert end_utility == 0.0, \"Die Utility des angegriffenen Kollektivs muss bei t=200 vollständig isoliert (0) sein.\"\n",
        "\n",
        "def test_ztil_normalzustand():\n",
        "    \"\"\"Überprüft, ob das System ohne Angriffsvektor stabil auf Maximalwert verbleibt.\"\"\"\n",
        "    end_utility = berechne_ztil_end_utility(staats_angriff=False, angriffs_zeitpunkt=50, sperr_haerte=6.0)\n",
        "    assert end_utility == 100.0, \"Ohne strukturellen Angriff darf keine automatische Utility-Absenkung stattfinden.\""
      ]
    }
  ]
}