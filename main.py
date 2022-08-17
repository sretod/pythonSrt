import pysrt
srt_path = 'VenomCarnage.srt'
subs = pysrt.open(srt_path)

for sub in subs:
    print(sub.text)
    print()
#test
#https://pypi.org/project/deep-translator/
#https://pypi.org/project/translate-api/