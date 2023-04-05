# ScrapingPython
# Web Scraping with Python from Beautiful Soup

![dataquest-learn-data-science-online](https://user-images.githubusercontent.com/90658763/183295433-364e925f-a8c9-472c-9aff-a3c1473094d9.gif)

- 1. Find Elements by ID.
- 2. Find Elements by HTML Class Name.
- 3. Extract Text From HTML Elements.
- 4. Find Elements by Class Name and Text Content.
- 5. Pass a Function to a Beautiful Soup Method.
- 6. Identify Error Conditions.
- 7. Access Parent Elements.
- 8. Extract Attributes From HTML Elements

![How-to-Build-a-Web-Scraping-Pipeline-in-Python-Using-BeautifulSoup](https://user-images.githubusercontent.com/90658763/183295561-55061f26-0b1a-4618-8954-ee951d362ad5.gif)


## Beautiful Soup Installation:

### -Open a windows terminal

Windows:
```console
pip install beautifulsoup4
```
```console
python setup.py install
 ```
### For more information

For Installation see [Installation website](https://code.tutsplus.com/es/tutorials/scraping-webpages-in-python-with-beautiful-soup-the-basics--cms-28211).

# Scrapingwebs:

## 1. Scrapy
[![Scrapy](https://user-images.githubusercontent.com/90658763/230072341-0383a9a3-6e43-488d-a285-cdbde55ea587.png)](https://scrapy.org/)
## 2. Heritrix
[![Heritrix](https://user-images.githubusercontent.com/90658763/230072897-85d73ba5-228c-46d1-b93d-589a9907efb6.png)](https://github.com/internetarchive/heritrix3/wiki)
## 3. Web-Harvest
[![Web-Harvest](https://user-images.githubusercontent.com/90658763/230073486-faf635ff-d282-4934-b0d5-0dd3ad85e4ba.png)](https://web-harvest.sourceforge.net/)
## 4. MechanicalSoup
[![Scrapy](https://user-images.githubusercontent.com/90658763/230073718-40dafde4-3a32-483f-a54c-41bf46e509e7.png)](https://mechanicalsoup.readthedocs.io/en/stable/)
## 5. Apify SDK
[![Apify SDK](https://user-images.githubusercontent.com/90658763/230074693-c29476c3-5568-40e1-8886-e630939850ad.gif)](https://apify.com/glenn/gif-scroll-animation/api)

 ```console
$ Node.js
>>> import { ApifyClient } from 'apify-client';

// Initialize the ApifyClient with API token
const client = new ApifyClient({
    token: '<YOUR_API_TOKEN>',
});

// Prepare actor input
const input = {
    "url": "https://crawlee.dev/",
    "proxyOptions": {
        "useApifyProxy": true
    },
    "frameRate": 7,
    "scrollPercentage": 10,
    "recordingTimeBeforeAction": 1000
};

(async () => {
    // Run the actor and wait for it to finish
    const run = await client.actor("glenn/gif-scroll-animation").call(input);

    // Fetch and print actor results from the run's dataset (if any)
    console.log('Results from dataset');
    const { items } = await client.dataset(run.defaultDatasetId).listItems();
    items.forEach((item) => {
        console.dir(item);
    });
})();
```

## 6. Apache Nutch

## 7. Jaunt

## 8. Node-crawler

## 9. PySpider

## 10. StormCrawler
