{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlit\n",
      "  Obtaining dependency information for streamlit from https://files.pythonhosted.org/packages/d3/96/9251b421d0a1c7d625a82a04bea56b8a9830c785940ec16db454b85c6db7/streamlit-1.29.0-py2.py3-none-any.whl.metadata\n",
      "  Downloading streamlit-1.29.0-py2.py3-none-any.whl.metadata (8.2 kB)\n",
      "Collecting altair<6,>=4.0 (from streamlit)\n",
      "  Obtaining dependency information for altair<6,>=4.0 from https://files.pythonhosted.org/packages/c5/e4/7fcceef127badbb0d644d730d992410e4f3799b295c9964a172f92a469c7/altair-5.2.0-py3-none-any.whl.metadata\n",
      "  Downloading altair-5.2.0-py3-none-any.whl.metadata (8.7 kB)\n",
      "Collecting blinker<2,>=1.0.0 (from streamlit)\n",
      "  Obtaining dependency information for blinker<2,>=1.0.0 from https://files.pythonhosted.org/packages/fa/2a/7f3714cbc6356a0efec525ce7a0613d581072ed6eb53eb7b9754f33db807/blinker-1.7.0-py3-none-any.whl.metadata\n",
      "  Downloading blinker-1.7.0-py3-none-any.whl.metadata (1.9 kB)\n",
      "Collecting cachetools<6,>=4.0 (from streamlit)\n",
      "  Obtaining dependency information for cachetools<6,>=4.0 from https://files.pythonhosted.org/packages/a2/91/2d843adb9fbd911e0da45fbf6f18ca89d07a087c3daa23e955584f90ebf4/cachetools-5.3.2-py3-none-any.whl.metadata\n",
      "  Downloading cachetools-5.3.2-py3-none-any.whl.metadata (5.2 kB)\n",
      "Requirement already satisfied: click<9,>=7.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (8.0.4)\n",
      "Requirement already satisfied: importlib-metadata<7,>=1.4 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (6.0.0)\n",
      "Requirement already satisfied: numpy<2,>=1.19.3 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (1.24.3)\n",
      "Requirement already satisfied: packaging<24,>=16.8 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (23.1)\n",
      "Requirement already satisfied: pandas<3,>=1.3.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (2.0.3)\n",
      "Requirement already satisfied: pillow<11,>=7.1.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (9.4.0)\n",
      "Collecting protobuf<5,>=3.20 (from streamlit)\n",
      "  Obtaining dependency information for protobuf<5,>=3.20 from https://files.pythonhosted.org/packages/ae/5b/7ed02a9b8e752c8f7bca8661779c0275b9e3e6a903a3045e6da51f796dda/protobuf-4.25.1-cp37-abi3-manylinux2014_x86_64.whl.metadata\n",
      "  Downloading protobuf-4.25.1-cp37-abi3-manylinux2014_x86_64.whl.metadata (541 bytes)\n",
      "Requirement already satisfied: pyarrow>=6.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (11.0.0)\n",
      "Requirement already satisfied: python-dateutil<3,>=2.7.3 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: requests<3,>=2.27 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (2.31.0)\n",
      "Collecting rich<14,>=10.14.0 (from streamlit)\n",
      "  Obtaining dependency information for rich<14,>=10.14.0 from https://files.pythonhosted.org/packages/be/be/1520178fa01eabe014b16e72a952b9f900631142ccd03dc36cf93e30c1ce/rich-13.7.0-py3-none-any.whl.metadata\n",
      "  Downloading rich-13.7.0-py3-none-any.whl.metadata (18 kB)\n",
      "Requirement already satisfied: tenacity<9,>=8.1.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (8.2.2)\n",
      "Requirement already satisfied: toml<2,>=0.10.1 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (0.10.2)\n",
      "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (4.7.1)\n",
      "Collecting tzlocal<6,>=1.1 (from streamlit)\n",
      "  Obtaining dependency information for tzlocal<6,>=1.1 from https://files.pythonhosted.org/packages/97/3f/c4c51c55ff8487f2e6d0e618dba917e3c3ee2caae6cf0fbb59c9b1876f2e/tzlocal-5.2-py3-none-any.whl.metadata\n",
      "  Downloading tzlocal-5.2-py3-none-any.whl.metadata (7.8 kB)\n",
      "Collecting validators<1,>=0.2 (from streamlit)\n",
      "  Obtaining dependency information for validators<1,>=0.2 from https://files.pythonhosted.org/packages/3a/0c/785d317eea99c3739821718f118c70537639aa43f96bfa1d83a71f68eaf6/validators-0.22.0-py3-none-any.whl.metadata\n",
      "  Downloading validators-0.22.0-py3-none-any.whl.metadata (4.7 kB)\n",
      "Collecting gitpython!=3.1.19,<4,>=3.0.7 (from streamlit)\n",
      "  Obtaining dependency information for gitpython!=3.1.19,<4,>=3.0.7 from https://files.pythonhosted.org/packages/8d/c4/82b858fb6483dfb5e338123c154d19c043305b01726a67d89532b8f8f01b/GitPython-3.1.40-py3-none-any.whl.metadata\n",
      "  Downloading GitPython-3.1.40-py3-none-any.whl.metadata (12 kB)\n",
      "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
      "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m30.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hRequirement already satisfied: tornado<7,>=6.0.3 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (6.3.2)\n",
      "Requirement already satisfied: watchdog>=2.1.5 in /home/yknam/anaconda3/lib/python3.11/site-packages (from streamlit) (2.1.6)\n",
      "Requirement already satisfied: jinja2 in /home/yknam/anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (3.1.2)\n",
      "Requirement already satisfied: jsonschema>=3.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (4.17.3)\n",
      "Requirement already satisfied: toolz in /home/yknam/anaconda3/lib/python3.11/site-packages (from altair<6,>=4.0->streamlit) (0.12.0)\n",
      "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Obtaining dependency information for gitdb<5,>=4.0.1 from https://files.pythonhosted.org/packages/fd/5b/8f0c4a5bb9fd491c277c21eff7ccae71b47d43c4446c9d0c6cff2fe8c2c4/gitdb-4.0.11-py3-none-any.whl.metadata\n",
      "  Downloading gitdb-4.0.11-py3-none-any.whl.metadata (1.2 kB)\n",
      "Requirement already satisfied: zipp>=0.5 in /home/yknam/anaconda3/lib/python3.11/site-packages (from importlib-metadata<7,>=1.4->streamlit) (3.11.0)\n",
      "Requirement already satisfied: pytz>=2020.1 in /home/yknam/anaconda3/lib/python3.11/site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3.post1)\n",
      "Requirement already satisfied: tzdata>=2022.1 in /home/yknam/anaconda3/lib/python3.11/site-packages (from pandas<3,>=1.3.0->streamlit) (2023.3)\n",
      "Requirement already satisfied: six>=1.5 in /home/yknam/anaconda3/lib/python3.11/site-packages (from python-dateutil<3,>=2.7.3->streamlit) (1.16.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in /home/yknam/anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (2.0.4)\n",
      "Requirement already satisfied: idna<4,>=2.5 in /home/yknam/anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (3.4)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /home/yknam/anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (1.26.16)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /home/yknam/anaconda3/lib/python3.11/site-packages (from requests<3,>=2.27->streamlit) (2023.11.17)\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from rich<14,>=10.14.0->streamlit) (2.2.0)\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from rich<14,>=10.14.0->streamlit) (2.15.1)\n",
      "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit)\n",
      "  Obtaining dependency information for smmap<6,>=3.0.1 from https://files.pythonhosted.org/packages/a7/a5/10f97f73544edcdef54409f1d839f6049a0d79df68adbc1ceb24d1aaca42/smmap-5.0.1-py3-none-any.whl.metadata\n",
      "  Downloading smmap-5.0.1-py3-none-any.whl.metadata (4.3 kB)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from jinja2->altair<6,>=4.0->streamlit) (2.1.1)\n",
      "Requirement already satisfied: attrs>=17.4.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (22.1.0)\n",
      "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /home/yknam/anaconda3/lib/python3.11/site-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: mdurl~=0.1 in /home/yknam/anaconda3/lib/python3.11/site-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.0)\n",
      "Downloading streamlit-1.29.0-py2.py3-none-any.whl (8.4 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.4/8.4 MB\u001b[0m \u001b[31m31.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hDownloading altair-5.2.0-py3-none-any.whl (996 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m996.9/996.9 kB\u001b[0m \u001b[31m38.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading blinker-1.7.0-py3-none-any.whl (13 kB)\n",
      "Downloading cachetools-5.3.2-py3-none-any.whl (9.3 kB)\n",
      "Downloading GitPython-3.1.40-py3-none-any.whl (190 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m190.6/190.6 kB\u001b[0m \u001b[31m45.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading protobuf-4.25.1-cp37-abi3-manylinux2014_x86_64.whl (294 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m294.6/294.6 kB\u001b[0m \u001b[31m45.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading rich-13.7.0-py3-none-any.whl (240 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m240.6/240.6 kB\u001b[0m \u001b[31m32.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading tzlocal-5.2-py3-none-any.whl (17 kB)\n",
      "Downloading validators-0.22.0-py3-none-any.whl (26 kB)\n",
      "Downloading gitdb-4.0.11-py3-none-any.whl (62 kB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m13.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
      "\u001b[?25hDownloading smmap-5.0.1-py3-none-any.whl (24 kB)\n",
      "Installing collected packages: validators, tzlocal, smmap, protobuf, cachetools, blinker, rich, pydeck, gitdb, gitpython, altair, streamlit\n",
      "Successfully installed altair-5.2.0 blinker-1.7.0 cachetools-5.3.2 gitdb-4.0.11 gitpython-3.1.40 protobuf-4.25.1 pydeck-0.8.1b0 rich-13.7.0 smmap-5.0.1 streamlit-1.29.0 tzlocal-5.2 validators-0.22.0\n"
     ]
    }
   ],
   "source": [
    "!pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2023-12-10 21:41:26.965 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run /home/yknam/anaconda3/lib/python3.11/site-packages/ipykernel_launcher.py [ARGUMENTS]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "\n",
    "st.title('Hello World')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
