var ts int

type Twitter struct {
	followees map[int]map[int]struct{}
	tweets    map[int]tweetsfeed
}

func Constructor() Twitter {
	return Twitter{
		followees: map[int]map[int]struct{}{},
		tweets:    map[int]tweetsfeed{},
	}
}

func (t *Twitter) PostTweet(userId int, tweetId int) {
	tweets, ok := t.tweets[userId]
	if !ok {
		tweets = tweetsfeed{}
	}
	ts++
	tweets = append(tweets, message{ts: ts, id: tweetId})
	t.tweets[userId] = tweets
}

func (t *Twitter) GetNewsFeed(userId int) []int {
	tweets, ok := t.tweets[userId]
	if !ok {
		tweets = tweetsfeed{}
	}
	tweets = tweets.getLast10()
	heap.Init(&tweets)
	followees := t.followees[userId]
	for k := range followees {
		followeetweets, ok := t.tweets[k]
		if !ok {
			continue
		}
		for _, t := range followeetweets.getLast10() {
			heap.Push(&tweets, t)
		}
	}
	return tweets.get10()
}

func (t *Twitter) Follow(followerId int, followeeId int) {
	if followeeId == followerId {
		return
	}
	followees, ok := t.followees[followerId]
	if !ok {
		followees = map[int]struct {
		}{
			followeeId: {},
		}
	} else {
		followees[followeeId] = struct{}{}
	}
	t.followees[followerId] = followees
}

func (t *Twitter) Unfollow(followerId int, followeeId int) {
	followees, ok := t.followees[followerId]
	if ok {
		delete(followees, followeeId)
	}
	t.followees[followerId] = followees
}

type message struct {
	ts int
	id int
}

type tweetsfeed []message

func (t tweetsfeed) Len() int            { return len(t) }
func (t tweetsfeed) Less(i, j int) bool  { return t[i].ts > t[j].ts }
func (t tweetsfeed) Swap(i, j int)       { t[i], t[j] = t[j], t[i] }
func (t *tweetsfeed) Push(x interface{}) { *t = append(*t, x.(message)) }
func (t *tweetsfeed) Pop() interface{} {
	old := *t
	n := len(old)
	x := old[n-1]
	*t = old[:n-1]
	return x
}

// fetches last 10 tweets (no heap)
func (t tweetsfeed) getLast10() []message {
	var msgs []message
	count := 0
	for i := len(t) - 1; i >= 0 && count < 10; i-- {
		msgs = append(msgs, t[i])
		count++
	}
	return msgs
}

func (t *tweetsfeed) get10() []int {
	var ids []int
	for t.Len() > 0 && len(ids) < 10 {
		ids = append(ids, heap.Pop(t).(message).id)
	}
	return ids
}
