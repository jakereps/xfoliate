<p align="center">
  <img src="http://cefns.nau.edu/~jk788/xfoliate/xfoliate.png"><br />
  <h5 align="center">exfoliate your face(book) with this one simple click.</h4>
</p>

---

[![Build Status](https://travis-ci.org/jakereps/xfoliate.svg?branch=master)](https://travis-ci.org/jakereps/xfoliate)

---

##### What is xfoliate?  
xfoliate is a Facebook history scrubber based on sentiment analysis.
##### Why xfoliate?
Don't hide your Facebook profile while on the job hunt. 9 out of 10 future doctors recommend xfoliate.

<p align="center">
  <h3 align="center">Coming 2016...</h3>
</p>

---

## Installation

Requirements:  
- [Anaconda w/ Python 3.5](https://www.continuum.io/downloads)

Setup:
```bash
git clone https://github.com/jakereps/xfoliate.git && cd xfoliate
conda create -n xfoliate python=3.5
source activate xfoliate
pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk
pip install .
```

---

## Usage

```bash
python -m xfoliate
```
