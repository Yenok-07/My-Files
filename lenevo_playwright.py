import requests

url = "https://flash.lenovo.com/gb/en/about/innovation/"

payload = {}
headers = {
  'authority': 'flash.lenovo.com',
  'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
  'authorization': 'Basic TGVub3ZvZmxhc2g6bWZDc3h6ZWZIWXUyb2NX',
  'cache-control': 'max-age=0',
  'cookie': 'bm_sz=D4749A6F042AE798831DA26B2E2DD1E3~YAAQRE/eF3FIGaKHAQAA1qrL4BOP9KMeT+cRprqVbt55hRzU3UK7hUo8Nxps9E7TG7e1s7papGHLBk0DdzPdYzj7kdgLN4d//oZdH3gU+aOCXGiPvSSl0IMJp662igD5iyDaQydLwnLB3+RuQEZ6IIf+Y8udyaPqXH+AOiDzVSf0LZMMmRBgwQeIlmBvdMAp9JDlv6qh5iLs07eCGxflPx3/mtDNBNthsTNcfJhLYI3Hkc+gfRL9PEVbn/vpMG4AHIk/sa6oPN7jKVcXcGXWOl3nwpDuOs15os6MI2CAPjO8+nA=~3424835~4408880; AMCV_F6171253512D2B8C0A490D45%40AdobeOrg=MCMID|40083544409017730970162208394448618405; leid=1.M+5dAzRu0qY; searchabran=53; s_eng_rfd=0.00; kndctr_F6171253512D2B8C0A490D45_AdobeOrg_identity=CiY0MDA4MzU0NDQwOTAxNzczMDk3MDE2MjIwODM5NDQ0ODYxODQwNVIRCL7hrob%2DMBABGAEqBElORDGgAdvhrob%2DMKgB87XFotTQw4oC8AG%2D4a6G%5FjA%3D; _ga=GA1.1.2075423228.1683103662; _evidon_consent_cookie={"consent_date":"2023-05-03T08:47:56.450Z","categories":{"6":{"advertising":true,"analytics":true,"social media":true,"essential":true}},"vendors":{"6":{"11":true,"51":true,"60":true,"66":true,"80":true,"81":true,"82":true,"103":true,"108":true,"242":true,"249":true,"257":true,"307":true,"342":true,"355":true,"395":true,"414":true,"457":true,"467":true,"480":true,"503":true,"642":true,"828":true,"831":true,"933":true,"942":true,"1028":true,"1272":true,"1647":true,"2191":true,"2253":true,"2450":true,"2468":true,"2516":true,"2521":true,"2594":true,"2884":true,"2937":true,"3042":true,"3058":true,"3490":true,"3778":true,"3857":true,"4464":true,"4748":true,"4941":true,"5104":true,"5296":true,"5304":true,"5678":true,"6359":true,"6531":true,"6609":true,"6638":true,"6877":true}},"cookies":{"6":true},"gpc":0,"consent_type":1}; has_consent_cookie=all; _fbp=fb.1.1683103678130.905292544; _gcl_au=1.1.534370275.1683103678; _tt_enable_cookie=1; _ttp=2TjVZc3Gv6y-42-mWL9XfXewVKU; usi_valid=true; QuantumMetricUserID=d47d99f2cdc5c366ded35254b98199f0; knexus_d13d58c021c52c7f020be3660bbea05b==cTO5IjN4kDO5EzX452a; AKA_A2=A; bm_mi=ED618DD61B886E253490ECCAF6A9C9D7~YAAQRE/eFyC/GqKHAQAAJIhj4RNTfJDygYPArwYmRZcfI7qfzKxiwP6fdZ/TWZb1IdgUCh/P6YPgrfabNbcVu1A/dqDZTKO9K5e1maypBb8p0IhUwCiNgaADBacaH42yvL4UHhMWUhAIhqWCGc/pnLMK8WaNyUNyO9mynfMxs20zCJcvBvzT7yl8B4J9ElwdqN+AYVMkdQod1wDm/TqVgZZOIhpPTQat0UEDBOLDN3JMWzq7L42BJoK9Dwe1srwOq4WkUjbLdY32Bz2hpRgRr1xqjERfLniKOvj6gBPBncnhJqCBQMhMVLv6gds+lUPEYRUI+5tMjzSy/Ih//zO907pgPESl6No2QTGqrWulGaS1RGchi5LpJ+2+~1; s_vnc365=1714649610310%26vn%3D3; inside-eu4=223921797-5b7663db33772baeebc93c218988d9e5ab64dc21f20a5f06201b3881c60021b7-0-0; ak_bmsc=E4B21FBBAC181E7B661F748971A7F481~000000000000000000000000000000~YAAQRE/eF02/GqKHAQAAm5Nj4RNLwj192W0FqsMA/raFj0JXsdDquAQb8Qy1KZ4mbTo8mHSXAfKOYP/pbuYHRhb6FG4CDn+10QCa1peOPTIY0iGQIPe+ZZF+X9RSGXrdqq1zwArWOsEP3uBV7ylqjTG5yFlnuXlleehihIfUTRpVDNd4OLA6Uy4ELRBC662GXY7vF/osQNHz3/nkjCTH9BWQ720eSVdSQZEVE3pvho1JkVXXOLHYMBQnX18yenoCeewfgToE9nBck3/MlzqeQOfhDg3/eoYTnaFwHNCWJP4VjLr11yiB8vWL9I8jTdVX4QxjIuL8uXepM9PuchYhdIQxe98Yz66r0NU5oQg4CQkBiXp7ITFnDthT6nLLHjf1XNWvdaGNoVUCtFE1v114v1KmSCGdH39iBgWJfhLsNYMw6/5D6utHlJHO5oI4BHZJ9/30QOqUHlfXiP6u/yF3E0wcWhdI4OEv; s_tslv=1683113735012; s_tot_rfd=2.07; mp_lenovo_gb_mixpanel=%7B%22distinct_id%22%3A%20%22187e0cc02531147-0fcddf8de54d28-26031b51-144000-187e0cc025415ea%22%2C%22bc_persist_updated%22%3A%201683103679061%7D; _page_type_=Brand%20Page; aamtest1=auto=549200; _mkto_trk=id:183-WCT-620&token:_mch-lenovo.com-1683103679095-11272; ln_or=eyI3MzE4IjoiZCJ9; bluecoreNV=true; kndctr_F6171253512D2B8C0A490D45_AdobeOrg_cluster=jpn3; _abck=2F0D2C40C6B420E7580B2C9737550878~0~YAAQxy43F5jk1qGHAQAAV6WE4QlnwvD03mr6OxaDC9cODpOHaVcucws5sMmOftw/eequdyoLrFBmadAByyCOZInJDcJ2iQpTiNWJT/cexpVSJVl4gATbXLjXcIK748RcTh5Quwq6AkKlz0UsNsiQTA4MqjN+33Hn6CcrwQlM67Yzb7mKmzS0z2Eso/B73BLIy/vte8ay3/gVSb3s/zEGj6aVM5uPJYJOQSru+IJH+L0rNKp2tZhOVfdNi8cSsf/HIZHsa2MEufwVeaNHeEBhw6Apwus6fXrMRTzxFcPQJNYAnqjXCEM29lvdtbhXxcju0He0Tyy8Y+PipoL0QyTA9rNh6i7TNxd5/5iTUwvB4IrwIHZeDJFblp7CaU46JoDauCTyFhsp3Bd+HqGWKk5pUpU6zFVxQGoR~-1~-1~1683119360; tfpsi=6c4f289d-98e0-4c6c-86ac-acd6b28234dc; bounceClientVisit5261v=N4IgNgDiBcIBYBcEQM4FIDMBBNAmAYnvgGZgCGKcAdGAKYB2A9gG6NUDGjAtkQOYBGRBkTL9GAVwREAlvSbMyCaY3pEQAGhAAnGCA0hpKAPq9GRlLRQpl9GMTJgLmwyYjnL1lXYcWAvkA; QuantumMetricSessionID=6c6dfe89be847e13438a8f604525d7bd; navposkey=services_nav; ftv_for_gben=%252Fservices%252F; inside-eu2=589901227-5c3ad7052e15115781d6f0a33747a2f365efbe11158353b83eb2cf10e7990b3e-0-0; exitsurveynotdisplayed=Incident%20check; aam_sc=aamsc=2525370|3245353|3526811|3730438|3245353|7238336|9039690|10170291|10863386|10997626|10170291; mp_dev_mixpanel=%7B%22distinct_id%22%3A%20%22187e167bb75d02-0bfea46332db19-26031b51-144000-187e167bb7619af%22%2C%22bc_persist_updated%22%3A%201683113884535%7D; _uetsid=34348f50e98f11ed8a1cbde641bd9c32; _uetvid=3434b120e98f11ed93f3e97043574595; _ga_LXNLK45HZF=GS1.1.1683115779.4.1.1683115867.0.0.0; _ga_XKJTHS007F=GS1.1.1683115779.4.1.1683115867.0.0.0; _ga_VBYSKTNF8V=GS1.1.1683115779.4.1.1683115867.0.0.0; _ga_K1R42ZM57S=GS1.1.1683115779.4.1.1683115867.0.0.0; knexus_8a732e0ed93a959059be7e5cb2803679=9JSNzATN2gTNxEzM4YTM3kTOyYDO5gTOx8Feut2Xkl2ciojIu9WazNXZz9FdzFGbiwiIxkTN4gzN1ETMzgjNxcTO5IjN4kDO5EzX452afRWazJiOi42bpN3clN3X05WZyJXdjJye; akavpau_WaitingRoomController=1683116840~id=6faa042dbc7354c43242078e71717549; bm_sv=23BE4B399E8D5D9196C1B6C8B84C22AE~YAAQDZHIF2rojd+HAQAAvkKQ4RMkKZiRSqBrA0rD1zXtBNVLQeDqmdLL/K8kUx7JjlJoZ6vzn+CmGrhWgeGDjoCprXM4ukuRTwuktW6T/ulMqgxIKgnTjjswRjtnJ+If94daIbsR8SaD04ZM8tYGtP1Cp03RifrpSgHQFyaFcnck7R8mZ+kdzKS+RERixYEWdfBPIJhKGel/fVmcQ4gbHkbEi5xsFy35l+rzBKqGmm74L8/QDwQNfWb7hsn22hic0Q==~1; RT="z=1&dm=lenovo.com&si=35ba52d7-1255-4269-b5cf-0c613592ab18&ss=lh7mjp6f&sl=0&tt=0&bcn=%2F%2F684d0d43.akstat.io%2F&ul=1l2va"; _abck=2F0D2C40C6B420E7580B2C9737550878~-1~YAAQCkIkFyIxH8OHAQAAV9+S4Qm+bSCptZ8NRlXhP3uALKt7bb3bw90zX1J6b8EVjkGjU5oN+CII+TX2R4/OdNTjYEJk5NvR0HYZIQH8KiJgJPkFkEXEUn31E+70vh466PTYM4YC4AxU58cnLq26JAc2/4HH3QjLiGs9NwwJWO36mSBBXm3KjPvspSPRncxQLUpXLzaxMg2Uqm5+1foO8WeedLhEJBilFxhUr+N9pOO9PWFbCTztsezVnWmUe7SvGUZ9HjjYg4pIj0TNJWtIJ2WToTZtN7Q+B4y2IuLCVdoBTRjDjupksskt4ldzafIyQieoL8jFCX7aOA6F6HyveAv8eFnhOaEGrmE5fVz6FsSFUGyvgrtg6YmkJ1v7gperhkvgopzktD9NFNwgqJtwar1UAX2WX4CQ~0~-1~1683119360; bm_sv=23BE4B399E8D5D9196C1B6C8B84C22AE~YAAQCkIkFyMxH8OHAQAAV9+S4RNGY+fwJX5zDq/KwdiKzrXde3bkgi2cJCBNuyac66MelXOIusz8KnrlWfeLvO06/8PukfMR64eQN7QZW40W5rrB+7/48iFmnixFRccz+6uL0yvoVDp4ClWILIc7vQk73pVl10mgtGiKOlCSjEL7sAM8CBxlK9jfSLYloE70fw89K8LuHjGd2rwY/OgQyjzKUzoyUZ4FX1lTW/j2eA56oadD5tkFtjzhom6fuQiqqA==~1; bm_sz=CB592D8E77726C3DA7E6306A233DA6A6~YAAQCkIkFyQxH8OHAQAAV9+S4RNuyuyh95GSEKg2Gqw67GHw5B2NoLMOqImA9N7ndM/szhr87qWA1uBFbI2OyppGRNRbalhcozwqszqwBQ1Xmb6jqA764QFe0JxjZlia+YyBWOwtUwtMKTL1+okqJ+GJo2Nm9VuRn6REIyGS072I4BFAF4wDVxaR3DizQsCErBcXRV3qnr4tI4MiB5kc54g+FsKEQ6/jkbk5D8+Or4i+GgsJyLCuDHWY535Am3r96mbdVpoOU0q/e0a1k0HvYfpZ7qJIRGJOUnDcEZwjYHcN2ZtaszayG+9n2nfq2gCssRlPUhd+DTdcKlY=~3618104~4277825; akavpau_WaitingRoomController=1683117011~id=b1b97d1f3a4b07414fab89d26a26b10c',
  'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'document',
  'sec-fetch-mode': 'navigate',
  'sec-fetch-site': 'none',
  'sec-fetch-user': '?1',
  'upgrade-insecure-requests': '1',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
}

response = requests.request("GET", url, headers=headers, data=payload)
breakpoint()

print(response.text)
