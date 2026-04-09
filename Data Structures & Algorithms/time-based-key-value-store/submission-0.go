type TimeMap struct {
	m map[string]ts
}

func Constructor() TimeMap {
	return TimeMap{m: map[string]ts{}}
}

func (tm *TimeMap) Set(key string, v string, t int) {
	values, ok := tm.m[key]
	if ok {
		values = append(values, timestamp{value: v, timestamp: t})
		tm.m[key] = values
		return
	}
	tm.m[key] = ts{timestamp{value: v, timestamp: t}}
}

func (tm *TimeMap) Get(key string, timestamp int) string {
	if len(tm.m) == 0 {
		return ""
	}
	values, ok := tm.m[key]
	if !ok {
		return ""
	}

	return values.search(timestamp)
}

type timestamp struct {
	timestamp int
	value     string
}

type ts []timestamp

func (ts ts) search(t int) string {
	L, R := 0, len(ts)-1
	var nearest timestamp
	for L <= R {
		mid := (L + R) / 2
		found := ts[mid]

		if found.timestamp == t {
			return found.value
		}
		if found.timestamp > t {
			R = mid - 1
		} else {
			if nearest.timestamp < found.timestamp {
				nearest = found
			}
			L = mid + 1
		}
	}
	return nearest.value
}
