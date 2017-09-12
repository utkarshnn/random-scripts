import asyncio
from aiohttp import ClientSession

def fetch(url, session):
    session.get(url) as response:
        return await response.read()

def run(r):
    urls = ['https://www.mrosupply.com/v-belts/urethane-flat-open-end-belting/154893_1032143_fenner-drives/',
'https://www.mrosupply.com/v-belts/1240620_12c345_gates-rubber/',
'https://www.mrosupply.com/v-belts/atv-belts/2788410_33c3836_gates-rubber/',
'https://www.mrosupply.com/v-belts/1986005_43vx475_jason-industrial/',
'https://www.mrosupply.com/v-belts/676633_a20_bando/',
'https://www.mrosupply.com/v-belts/676664_a51_bando/',
'https://www.mrosupply.com/v-belts/urethane-open-end-v-belting/155045_4940065_fenner-drives/',
'https://www.mrosupply.com/v-belts/linked-open-end-v-belting/668057_0418033_fenner-drives/',
'https://www.mrosupply.com/v-belts/678265_5l680_bando/',
'https://www.mrosupply.com/v-belts/urethane-open-end-v-belting/154873_1032031_fenner-drives/',
'https://www.mrosupply.com/v-belts/urethane-open-end-v-belting/154881_1032047_fenner-drives/',
'https://www.mrosupply.com/v-belts/urethane-flat-open-end-belting/154897_1032155_fenner-drives/',
'https://www.mrosupply.com/v-belts/urethane-open-end-v-belting/154876_1032038_fenner-drives/',
'https://www.mrosupply.com/v-belts/678174_4l550_bando/',
'https://www.mrosupply.com/v-belts/variable-speed-belts/1996920_28x8x800_jason-industrial/',
'https://www.mrosupply.com/v-belts/678074_3l170_bando/',
'https://www.mrosupply.com/v-belts/welding-tools-for-open-end-belting/817627_5700160k_fenner-drives/',
'https://www.mrosupply.com/v-belts/681217_5m710_bando/',
'https://www.mrosupply.com/v-belts/2021852_r3vx750-3_carlisle-pt/',
'https://www.mrosupply.com/v-belts/urethane-round-open-end-belting/154865_1032008_fenner-drives/',
'https://www.mrosupply.com/v-belts/2018212_dp132_carlisle-pt/',
'https://www.mrosupply.com/v-belts/linked-open-end-v-belting/668054_0410070_fenner-drives/',
'https://www.mrosupply.com/v-belts/welding-tools-for-open-end-belting/154802_5700227_fenner-drives/',
'https://www.mrosupply.com/v-belts/2003910_3vx720_jason-industrial/',
'https://www.mrosupply.com/v-belts/urethane-round-open-end-belting/154925_4907024_fenner-drives/',
'https://www.mrosupply.com/v-belts/welding-tools-for-open-end-belting/817601_5700233_fenner-drives/',
'https://www.mrosupply.com/v-belts/2009118_n267805_jason-industrial/',
'https://www.mrosupply.com/v-belts/2017366_a37_carlisle-pt/',
'https://www.mrosupply.com/v-belts/urethane-flat-open-end-belting/154895_1032148_fenner-drives/',
'https://www.mrosupply.com/v-belts/2017667_bb92_carlisle-pt/',
'https://www.mrosupply.com/v-belts/linked-open-end-v-belting/817564_l02b5_fenner-drives/',
'https://www.mrosupply.com/v-belts/urethane-open-end-v-belting/155026_4940030_fenner-drives/',
'https://www.mrosupply.com/v-belts/676635_a22_bando/',
'https://www.mrosupply.com/v-belts/2017992_bp77_carlisle-pt/',
'https://www.mrosupply.com/v-belts/675578_3b148_bando/',
'https://www.mrosupply.com/v-belts/urethane-round-open-end-belting/154869_1032018_fenner-drives/',
'https://www.mrosupply.com/v-belts/676842_b94_bando/',

]

    tasks = []

    # Fetch all responses within one Client session,
    # keep connection alive for all requests.
    ClientSession() as session:
        for i in range(r):
            task = asyncio.ensure_future(fetch(url.format(i), session))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)
        # you now have all response bodies in this variable
        print(responses)

def print_responses(result):
    print(result)

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(4))
loop.run_until_complete(future)
