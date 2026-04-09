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
	if len(folders) == 0 {
        return "/"
    }
    return "/"+strings.Join(folders, "/")
}

func cmdOrFolder(b *strings.Builder, folders []string) []string {
	if b.Len() == 0 {
		return folders
	}
	str := b.String()
	b.Reset()
	if str == "." {
		return folders
	}
	if str == ".." {
		if len(folders) > 0 {
			folders = folders[:len(folders)-1]
		}
		return folders
	}
	return append(folders, str)
}