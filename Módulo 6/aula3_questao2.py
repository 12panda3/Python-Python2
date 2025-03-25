dominios = []
sites = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = [i[4:-4] for i in sites]

print(dominios)