# https://leetcode-cn.com/problems/design-twitter/

import time
import queue


class Tweet:
    def __init__(self, post_id):
        self.tweet_id = post_id
        self.post_time = int(time.time() * 1000)
        self.next = None

    # 重置小于符号，方便后来的优先队列比较对象大小。由于优先队列默认POP小的元素，所以我们需要设置成POP大的元素（时间越往后，时间戳大）
    # 所以此处设置为 “>” , 也就是，self.post_time > other.post_time
    def __lt__(self, other):
        return self.post_time > other.post_time


class TweetList:
    def __init__(self):
        self.head = Tweet(-1)
        self.length = 0

    def add_tweet(self, tweet: Tweet):
        tmp = self.head.next
        self.head.next = tweet
        tweet.next = tmp
        self.length += 1

    def show(self):
        tweet = self.head.next
        while tweet:
            print(tweet.tweet_id)
            tweet = tweet.next


class User:
    def __init__(self, user_id):
        self.user_id = user_id
        # 使用集合（Set）这种数据结构来存，因为不能重复，而且需要快速查找
        self.follows = {self.user_id}
        self.tweet_list = TweetList()

    def post(self, post_id):
        self.tweet_list.add_tweet(Tweet(post_id))

    def follow(self, user_id):
        self.follows.add(user_id)

    def unfollow(self, user_id):
        # 判断是否存在，并且不能取关自己
        if user_id != self.user_id and user_id in self.follows:
            self.follows.remove(user_id)


class Twitter:
    def __init__(self):
        # id -> user的映射
        self.user_dict: {int: User} = {}

    def post_tweet(self, user_id, tweet_id):
        if user_id not in self.user_dict.keys():
            user = User(user_id)
            user.post(tweet_id)
            self.user_dict[user_id] = user
        else:
            self.user_dict[user_id].post(tweet_id)

    def get_news_feed(self, user_id):
        result = []
        # 优先队列pq
        pq = queue.PriorityQueue()
        if user_id not in self.user_dict.keys():
            return result
        users = self.user_dict[user_id].follows
        # pq插入每个tweet_list的第一个元素
        for user in users:
            pq.put(self.user_dict[user].tweet_list.head.next)
        while not pq.empty():
            # 满足10个结束返回
            if len(result) == 10:
                break
            twt = pq.get()
            print("----", twt.tweet_id)
            result.append(twt.tweet_id)
            # 删除弹出的元素，并且将之后的元素接着放到优先队列中比较
            if twt.next is not None:
                pq.put(twt.next)
        return result

    def follow(self, follower_id, followee_id):
        if follower_id not in self.user_dict.keys():
            user = User(follower_id)
            self.user_dict[follower_id] = user

        if followee_id not in self.user_dict.keys():
            user = User(followee_id)
            self.user_dict[followee_id] = user
        self.user_dict[follower_id].follow(followee_id)

    def unfollow(self, follower_id, followee_id):
        if follower_id in self.user_dict.keys() and followee_id in self.user_dict.keys():
            self.user_dict[follower_id].unfollow(followee_id)


# time.sleep(0.1)是为了让时间戳不一样，产生时间间隔
twitter = Twitter()
twitter.post_tweet(1, 1)
time.sleep(0.01)
twitter.post_tweet(1, 2)
time.sleep(0.01)
twitter.post_tweet(1, 3)
time.sleep(0.01)
twitter.post_tweet(1, 4)
time.sleep(0.01)
twitter.post_tweet(2, 5)
time.sleep(0.01)
twitter.post_tweet(2, 6)
time.sleep(0.01)
twitter.post_tweet(3, 7)

twitter.follow(1, 2)
print(twitter.get_news_feed(1))

twitter.unfollow(1, 2)
print(twitter.get_news_feed(1))

twitter.unfollow(1, 2)
print(twitter.get_news_feed(1))

twitter.follow(1, 2)
twitter.follow(1, 3)
print(twitter.get_news_feed(1))
