#!/usr/bin/env python
from random import choice


def word():
    word_list = (
        # 艾尔文
        "最好的学习, 就是不断的练习.",
        "你未来会过得如何, 取决于你现在如何去过.",
        "每一件事的成功, 都是有迹可循的, 失败也是.",
        "对每个人来说, 每天, 每年的时间长度都是固定的, 但如何运用, 是你自己决定的.",
        "我们无法决定别人如何看待自己, 但我们永远有能力决定, 要成为什么样的自己.",
        "再大的梦想, 都是从一个起点开始; 再远的路, 都是从每一小步的累积. 不要小看你走的每一步, 因为它正在决定你的人生道路.",
        "渴望学习, 同时努力练习. 然后不要害怕犯错. 因为犯错的过程, 通常就是成长的过程.",
        "成功的关键, 不在于能否走对路, 而是能否走过很多的路. 所谓的卓越, 也不是要比别人优秀, 而是要超越自己.",
        "人的一生, 会由很多个选择来决定. 只是除非你知道自己为了什么做选择, 否则其实你就是, 没在做选择.",
        "人生有很多重要的事, 但记得不是每一件事都很重要. 忙碌之余要停下来思考, 现在过的生活, 是不是当初自己想过的生活; 未来想走的路, 是不是连结到脚下正在走的路.",
        "想要改变人生, 你要先改变每年做的事. 想要改变每年做的事, 你要先改变看待今天的方式.",
        "如果你不行动, 最好的情况就只是现在. 如果你行动了, 最坏的情况也不过是现在. 所以, 你在担心什么?",
        "关于人生, 近看往往是一条路, 远看其实可以有很多条. 也许你现在, 还不是走在喜欢的那条路上, 但记得, 不要放弃通往那条路的任何可能.",
        "每个人的一生, 都是专属自己的旅程. 不要因为人喜好比较的天性, 而忘记自己是为了什么在努力.",
        "时间重不重要, 要看你认为它重不重要. 你越重视它, 他会给你越多的东西; 你越忽略它, 他会带走越多你想要的事情.",
        "改变, 不会是一朝一夕就发生, 却肯定是一点一滴进步而积累. 每天让自己比昨天更好一点, 每个明天就会比今天更好一些.",
        "一个人是否快乐, 取决的不是那件事如何发生, 而是你如何看待那件事的发生.",
        "人一辈子的时间有限, 宁可因为喜欢的事情而耗掉时间, 也不要因为讨厌的事情而错过时间.",
        "人生, 有高峰就有低谷, 有困难也会有惊喜. 记得, 你现在人在哪里不重要, 重要的是你打算将来要去哪里.",
        "一件事情的好坏, 影响的不只是事情的本身, 更是你用什么心情看待. 希望你也能相信, 改变自己的心态, 就可以改变自己的人生.",

        # 偏指
        "怕麻烦是学习新知识的最大障碍. 准备好心态, 一头扎进最复杂的内容里. 这样才能获得新的东西.",
        "人可以选择任何适合的方式去解决问题, 或者是认输直接承代价, 唯独逃避是最难看且无用的.",
        "加油吧, 希望咱们都能完整的走出大洋国.",
        # Dolltator
        "所以我会要求自己随时保持谦卑, 虚心听取他人的意见, 不断突破舒适区去学习新的知识, 绝不自以为是.",
        # 神隐少女
        "人生就是一列开往坟墓的列车，路途上会有很多站，很难有人可以自始至终陪着走完。当陪你的人要下车时，即使不舍也该心存感激，然后挥手道别。",
        "不管前方的路有多苦，只要走的方向正确，不管多么崎岖不平，都比站在原地更接近幸福。",
        "我只能送你到这里了，剩下的路你要自己走，不要回头。",
        "用善意的心情去理解别人的话，会让世界单纯美好容易。世界如此之大，我却能幸运地遇见一些人。",
        "我不知道将去何方，但我已在路上。",
        # 猫的报恩
        "你不能等待别人来安排你的人生；自己想要的，自己争取。",
        "心只有一颗，别让它沉浸悲伤。",
        "如果你遇到了有点不可思议又让你困扰的事，不妨去探一探究竟。",
        "我始终相信，在这个世界上，一定有另一个自己，在做着我不敢做的事，在过着我想过的生活。",
        "你应该要学着做你自己，面对真实的自我，只要做到这一点你就什么都不用惧怕。",
        # 風之谷
        "好梦向来易醒。",
        "你不能改变命运，但你可以选择原地等待，或是，勇敢面对。",
        "坚强不是面对悲伤不流一滴泪，而是擦干眼泪后微笑着面对以后的生活。",
        # 天空之城
        "有时候，坚持了你最不想干的事情之后，便可得到你最想要的东西。",
        # 魔女宅急便
        "只有一个人在旅行时，才听得到自己的声音，它会告诉你，这世界比想象中的宽阔。",
        "在这个世界上别太依赖任何人，因为当你在黑暗中挣扎时，连你的影子都会离开你。",
        "不要对外表过分在意，心灵才是最重要的。",
        # 名言佳句
        "It's better to light a candle than curse the darkness.",
        "Move in silence, only speak when it’s time to say Checkmate.",
        "在初学者的头脑中有很多可能性，在专家的头脑中，可能性很少。——铃木俊隆"
    )
    msg = choice(word_list)
    # msg = word_list[-1]
    return msg


def read_site():
    site_list = (
        ("科学上网", 'https://haoel.github.io/'),
        ("阮一峰网络日志", 'http://www.ruanyifeng.com/blog/'),
        ("编程随想的博客", 'https://program-think.blogspot.com/'),
        ("秋水逸冰", 'https://teddysun.com/'),
        ("逗比根据地(镜像站)", 'https://doubibackup.com/'),
        ("OI Wiki", 'https://oi-wiki.org/'),
    )
    content = {"content": site_list}
    return content


def hidden_site():
    site_list = (
        ("生成短链接", "https://app.bitly.com/"),
        ("文件分享(自动失效)", "https://send.firefox.com"),
        ("加密消息(自动失效)", "https://temp.pm/"),
        ("接收邮件", "https://temp-mail.org/"),
        ("接收短信", "https://smsreceivefree.com/"),
        ("接收短信(包括 +86)", "https://www.pdflibr.com/"),
        ("生成 UUID", "https://www.uuidgenerator.net/"),
        ('生成"真人"头像', "https://thispersondoesnotexist.com/"),
        ("生成个人信息(美国公民)", "https://www.fakenamegenerator.com/"),
        ("Discord 在线聊天室", "https://discordapp.com/"),
    )
    content = {"content": site_list}
    return content


def random_index_html():
    # index_list = ['index_1.html', 'index_2.html', 'index_3.html', 'index_4.html']
    # prob = [3, 3, 3, 1]
    index_list = (
        "index_1.html", "index_1.html", "index_1.html",
        "index_2.html", "index_2.html", "index_2.html",
        "index_3.html", "index_3.html", "index_3.html",
        "index_4.html",
        "index_5.html",
        # "index_6.html",
        # "index_7.html",
    )
    # return render(request, choices(index_list, prob), content)  # 3.7 新特性
    return choice(index_list)


if __name__ == '__main__':
    print(word())
