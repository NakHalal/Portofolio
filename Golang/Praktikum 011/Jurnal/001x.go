package main

import "fmt"

const NMAX = 1000

var list playlist
var song lagu

type lagu struct {
	title, artist string
	durasi        waktu
}
type waktu struct {
	menit, detik int
}
type playlist = [NMAX]lagu

func carilagu(T playlist, title, artist string, n int) bool {
	var found bool
	i := 0
	found = false
	for i < n && n > 0 && !found {
		found = (T[i].title == title) && (T[i].artist == artist)
		i++
	}
	return found
}

func buatPlaylist(T *playlist, n *int) {
	var title, artist string
	var durasi waktu
	var song lagu

	fmt.Println("Input judul, penyanyi, menit, dan detik (berurutan)")
	fmt.Println("---------------------------------------------------")
	fmt.Scanln(&title, &artist, &durasi.menit, &durasi.detik)
	for title != "#" && artist != "#" && *n <= NMAX-1 {
		if !carilagu(*T, title, artist, *n) {
			T[*n] = song
			song.title = title
			song.artist = artist
			song.durasi = durasi
			*n++
		}
		fmt.Scanln(&title, &artist, &durasi.menit, &durasi.detik)
	}
}

func terlama(T playlist, n int) int {
	var detik1, detik2 int
	var x, y waktu
	i := 0
	hasil := 0
	for i < n && n > 0 {
		if i == 0 {
			x = T[i].durasi
		} else {
			y = T[i].durasi
			detik1 = (x.menit * 60) + x.detik
			detik2 = (y.menit * 60) + y.detik
			if detik2 > detik1 {
				hasil = i
				x = y
			}
		}
		i++
	}
	return hasil
}

func cetakPlaylist(T playlist, n int) {
	var i, x int
	i = 0
	for i < n {
		x = terlama(list, n)
		if i == x {
			fmt.Println("*", T[i].title, T[i].durasi.menit, " menit ", T[i].durasi.detik, " detik")
		} else {
			fmt.Println(T[i].title)
		}
		i++
	}
}

func main() {
	n := 0
	buatPlaylist(&list, &n)
	cetakPlaylist(list, n)
}
