def get_all_links(page):
    links = [];
    while True:
        url, endpos = get_next_target(page);
        if url:
            links.append(url);
            page = page[endpos:];
        else:
            break;
    return links;


#depth first page;
def crawl_web (seed):
    toCrawl = [seed];
    crawled = [];
    while toCrawl:
        page = toCrawl.pop();
        if page not in crawled:
            
    return crawled;