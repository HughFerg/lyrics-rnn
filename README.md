# Tensorflow word rnn optimized for song lyrics from Genius.com

Multi-layer Recurrent Neural Networks (LSTM, RNN) for word-level language models in Python using TensorFlow.
This setup is based on language modeling for music lyrics, taken from https://genius.com from the artists selected in scrape.py.

Mostly reused code from https://github.com/hunkim/word-rnn-tensorflow which was mostly reused code from https://github.com/sherjilozair/char-rnn-tensorflow which was inspired from Andrej Karpathy's [char-rnn](https://github.com/karpathy/char-rnn).

Also built using the Genius lyrics scraping interface from https://github.com/johnwmillr/LyricsGenius

# Requirements
- Tensorflow, install via pip:
```bash 
pip3 install tensorflow
```
- Currently optimized for Python 3.6
- Lyricsgenius package, install via pip:
```bash
pip3 install lyricsgenius
```

# Basic Usage
To scrape lyrics from specified artists, add your Genius API key to the top of scrape.py. Then, in the same file, enter the artist names: 
```
artists = [
    'Micheal Jackson',
    'Mac Miller',
    'Herbie Hancock',
    'The Weeknd'
]
```
Then run 
```bash
python3 scrape.py
```
to get lyrics from all songs on the Genius website for the specified artists. Max # of songs per artist can be specified as such in scrape.py:
```
artist = api.search_artist(artist_name, max_songs=200)
```
Note: This implementation is still buggy, and occasionally will timeout for reasons still being worked out. If so, simply running the script again (and removing the artists that were already pulled from to reduce repetition) will fix.

Now, all lyrics should be in the data/input.txt file.

To train with default parameters on the rap-lyrics corpus, run:
```bash
python3 train.py
```
Note: depending on the size of your dataset, this process will likely take a significant amount of time.

To sample from a trained model
```bash
python3 sample.py
```

To pick using beam search, use the `--pick` parameter. Beam search can be
further customized using the `--width` parameter, which sets the number of beams
to search with. For example:
```bash
python3 sample.py --pick 2 --width 4
```
