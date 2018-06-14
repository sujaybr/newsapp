from getExtraCategoriesNamesFromDB import getAllCategories
from wikiGetData import getWikiData
from gatherNewsDataFromRssFeedsForACategory import scrapeForWordAndCat
from news_classifier_api import categorizeApi

old = []
while(True):
    try:
        categories = getAllCategories()
        # categories = ['cricket']
        for i in categories:
            if i not in old:
                old.append(i)
                print (i)
                wikidata = getWikiData(i)
                print (wikidata)

                category = categorizeApi(wikidata)
                scraped_data = scrapeForWordAndCat(category, i)
                # print (scraped_data)
            else:
                print "waiting for more categories"
    except:
        print "An error occured"
