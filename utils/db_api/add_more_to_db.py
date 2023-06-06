from sys import platform
import sqlite3

data = """https://vk.com/vinekkislota?z=video-182744885_456239825%2Fpl_-182744885_-2 2023-04-2204:57:07.669413	clips/video182744885_4562398252Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239820%2Fpl_-182744885_-2	2023-04-2204:57:24.245755	clips/video182744885_4562398202Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239814%2Fpl_-182744885_-2	2023-04-2205:30:50.297964	clips/video182744885_4562398142Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239809%2Fpl_-182744885_-2	2023-04-2205:31:03.952118	clips/video182744885_4562398092Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239689%2Fpl_-182744885_-2	2023-04-2205:31:11.734013	clips/video182744885_4562396892Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239685%2Fpl_-182744885_-2	2023-04-2205:31:18.360871	clips/video182744885_4562396852Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239651%2Fpl_-182744885_-2	2023-04-2205:31:41.076964	clips/video182744885_4562396512Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239469%2Fpl_-182744885_-2	2023-04-2205:31:55.658201	clips/video182744885_4562394692Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239182%2Fpl_-182744885_-2	2023-04-2205:32:13.412122	clips/video182744885_4562391822Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239173%2Fpl_-182744885_-2	2023-04-2205:32:23.390530	clips/video182744885_4562391732Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239166%2Fpl_-182744885_-2	2023-04-2205:32:39.385987	clips/video182744885_4562391662Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239162%2Fpl_-182744885_-2	2023-04-2205:32:51.464136	clips/video182744885_4562391622Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239157%2Fpl_-182744885_-2	2023-04-2205:33:07.088506	clips/video182744885_4562391572Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239154%2Fpl_-182744885_-2	2023-04-2205:33:21.795897	clips/video182744885_4562391542Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239153%2Fpl_-182744885_-2	2023-04-2205:33:30.898703	clips/video182744885_4562391532Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239152%2Fpl_-182744885_-2	2023-04-2205:33:39.570634	clips/video182744885_4562391522Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239141%2Fpl_-182744885_-2	2023-04-2205:34:00.949943	clips/video182744885_4562391412Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239132%2Fpl_-182744885_-2	2023-04-2205:34:15.366186	clips/video182744885_4562391322Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239130%2Fpl_-182744885_-2	2023-04-2205:34:39.368707	clips/video182744885_4562391302Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239125%2Fpl_-182744885_-2	2023-04-2205:34:56.235373	clips/video182744885_4562391252Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239111%2Fpl_-182744885_-2	2023-04-2205:35:10.474433	clips/video182744885_4562391112Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239106%2Fpl_-182744885_-2	2023-04-2205:35:36.512896	clips/video182744885_4562391062Fpl_182744885_2.mp4 
https://vk.com/vinekkislota?z=video-182744885_456239099%2Fpl_-182744885_-2	2023-04-2205:35:43.714457	clips/video182744885_4562390992Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239097%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:40:27.555880	clips/video182744885_4562390972Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239096%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:41:23.130537	clips/video182744885_4562390962Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239088%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:41:42.354912	clips/video182744885_4562390882Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239086%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:41:48.213152	clips/video182744885_4562390862Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239080%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:42:18.005903	clips/video182744885_4562390802Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239075%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:42:48.671254	clips/video182744885_4562390752Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239074%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:43:02.007166	clips/video182744885_4562390742Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239073%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:43:07.474490	clips/video182744885_4562390732Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239070%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:44:03.703846	clips/video182744885_4562390702Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239067%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:44:28.249866	clips/video182744885_4562390672Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239066%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:44:33.920194	clips/video182744885_4562390662Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239065%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:45:03.817584	clips/video182744885_4562390652Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239061%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:45:40.487140	clips/video182744885_4562390612Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239060%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:45:47.061371	clips/video182744885_4562390602Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239055%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:46:34.680204	clips/video182744885_4562390552Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/video/@vinekkislota?z=video-182744885_456239047%2Fclub182744885%2Fpl_-182744885_-2	2023-04-2205:46:52.959867	clips/video182744885_4562390472Fclub1827448852Fpl_182744885_2.mp4 
https://vk.com/youngkill6?z=video-165858696_456239026%2Fvideos-165858696%2Fpl_-165858696_-2	2023-04-2205:52:59.287303	clips/video165858696_4562390262Fvideos1658586962Fpl_165858696_2.mp4 
https://vk.com/video/@youngkill6?z=video-165858696_456239022%2Fclub165858696%2Fpl_-165858696_-2	2023-04-2205:53:20.049407	clips/video165858696_4562390222Fclub1658586962Fpl_165858696_2.mp4 """

def connect_db():
    print(platform)
    if platform == "linux" or platform == "linux2":
        conn = sqlite3.connect("/usr/local/bin/botwithclips/utils/db_api/user.db")
        return conn
    elif platform == "win32":
        conn = sqlite3.connect("C:\\Users\\KENT SZ\\PycharmProjects\\botwithclips\\utils\\db_api\\user.db")
        return conn

def add_more_to_db(category, link, upload_date, path):
    sql = """INSERT INTO videos(category, link, upload_date, path) VALUES (?, ?, ?, ?)"""
    db = connect_db()
    db.cursor().execute(sql, (category, link, upload_date, path))
    db.commit()
    db.close()


def create_list(data):
    datas = data.replace("\t", " ")
    datas = datas.replace("\n", "")
    datas = datas.split(" ")
    print(datas)
    for e in datas:
        elements = []
        elements.append(datas[0])
        elements.append(datas[1])
        elements.append(datas[2])
        datas.remove(elements[0])
        datas.remove(elements[1])
        datas.remove(elements[2])
        print(elements)
        add_more_to_db("input", elements[0], elements[1], elements[2])
    print(datas)


if __name__ == "__main__":
    create_list(data)