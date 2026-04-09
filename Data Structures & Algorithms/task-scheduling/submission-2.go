func leastInterval(ts []byte, n int) int {
	m := map[byte]int{}
	for _, t := range ts {
		m[t]++
	}
	var scheduler tasks
	for k, v := range m {
		heap.Push(&scheduler, sumTask{task: k, times: v})
	}

	var cycles int
	for {
		var (
			executed tasks
		)
		for scheduler.Len() > 0 && len(executed) < n+1 {
			task := heap.Pop(&scheduler).(sumTask)
			task.times--
			executed = append(executed, task)
		}
		if len(executed) == 0 {
			break
		}
		for _, e := range executed {
			if e.times > 0 {
				heap.Push(&scheduler, e)
			}
		}
		if scheduler.Len() > 0 {
			cycles += n + 1
		} else {
			cycles += len(executed)
		}
	}

	return cycles
}

type sumTask struct {
	task  byte
	times int
}

type tasks []sumTask

func (t tasks) Less(i, j int) bool {
	return t[i].times > t[j].times
}

func (t tasks) Swap(i, j int) {
	t[i], t[j] = t[j], t[i]
}

func (t tasks) Len() int {
	return len(t)
}

func (t *tasks) Push(task interface{}) {
	*t = append(*t, task.(sumTask))
}

func (t *tasks) Pop() interface{} {
	old := *t
	x := old[len(old)-1]
	*t = old[:len(old)-1]
	return x
}
