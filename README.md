## Help us download structures for our UVC project!

1. Make sure you have Google Chrome installed (tested on 114.0.5735.198)
2. Install [uBlock origin](https://ublockorigin.com/) (otherwise ads take forever to load)
3. Run `pip install -r requirements.txt`
4. Run `python chemscrape_based.py [number]`, where [number] is your assigned download offset (see below)
5. Accept the cookies banner
6. Send the downloaded `.mol` files, as well as `errors.txt`, to hello@cavendishlabs.org

Thank you!!


### Download offsets


| Offset | Person       |
|-------:|-------------|
|   0    | [this could be you!]         |
|   300  | [this could be you!]       |
|   600  | [this could be you!]       |
|   900  | Derik       |
|   1200  | [this could be you!]       |
|   1500  | [this could be you!]       |


### Troubleshooting

#### `ValueError: There is no such driver by url https://chromedriver.storage.googleapis.com/LATEST_RELEASE_115.0.5790`

Replace line 14 with `chrome_path = ChromeDriverManager(version='114.0.5735.198').install()`.

#### My version of Chrome is too new!

You can use firefox instead, by running `chemscrape_based_ff.py` instead of `chemscrape_based.py`
