url = "http://dl.dropbox.com/u/7334460/Magick_py/magic.pdf"
print(url[url.rindex("/")+1:])

# --- 2 case ----
print(url[url.rfind("/")+1:])