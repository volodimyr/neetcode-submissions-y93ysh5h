func simplifyPath(path string) string {
	folders := []string{}
	var b strings.Builder
	for _, p := range path[1:] {
		if p != '/' {
			b.WriteRune(p)
			continue
		}
		folders = cmdOrFolder(&b, folders)
	}
	folders = cmdOrFolder(&b, folders)
	b.WriteRune('/')
	b.WriteString(strings.Join(folders, "/"))
	return b.String()
}

func cmdOrFolder(b *strings.Builder, folders []string) []string {
	fmt.Println("b = ", b.String())
	if b.Len() == 0 {
		return folders
	}
	switch b.String() {
	case ".":
	case "..":
		if len(folders) != 0 {
			folders = folders[:len(folders)-1]
		}
	default:
		folders = append(folders, b.String())
	}
	b.Reset()
	return folders
}
