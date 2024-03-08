import requests

def count_words(subreddit, word_list,):
    word_count={}
    after=None
    if not word_list:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 100, 'after': after}
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            children = data['data']['children']
            for child in children:
                title = child['data']['title'].lower()
                for word in word_list:
                    if word.lower() in title.split():
                        if word.lower() in word_count:
                            word_count[word.lower()] += 1
                        else:
                            word_count[word.lower()] = 1

            after = data['data']['after']
            if after:
                count_words(subreddit, word_list)
            else:
                sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
                for word, count in sorted_word_count:
                    print(f"{word}: {count}")
