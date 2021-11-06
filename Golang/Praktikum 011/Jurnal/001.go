package main

import "fmt"

const NMAX int = 1000

type waktu struct {
	minute int
	second int
}
type lagu struct {
	title    string
	artist   string
	duration waktu
}
type playlist struct {
	database [NMAX - 1]lagu
	sum      int
}

func buatPlaylist(PlaylistDoc *playlist, n *int) {
	var TL lagu
	fmt.Scanln(&TL.title, &TL.artist, &TL.duration.minute, &TL.duration.second)

	for (TL.title != "#") && (TL.artist != "#") {
		if SearchSong(TL.title, TL.artist, *PlaylistDoc) == -1 {
			PlaylistDoc.database[*n].title = TL.title
			PlaylistDoc.database[*n].artist = TL.artist
			PlaylistDoc.database[*n].duration.minute = TL.duration.minute
			PlaylistDoc.database[*n].duration.second = TL.duration.second

			*n = *n + 1
		}
		fmt.Scanln(&TL.title, &TL.artist, &TL.duration.minute, &TL.duration.second)
	}
}

func SearchSong(title string, artist string, PlaylistDoc playlist) int {
	var i int
	var found bool

	i = 0
	found = false
	for i < PlaylistDoc.sum && PlaylistDoc.sum > 0 && !found {
		found = (PlaylistDoc.database[i].title == title) && (PlaylistDoc.database[i].artist == artist)
		i++
	}
	if found == true {
		return i
	} else {
		return -1
	}
}

func cetakPlaylist(PlaylistDoc playlist, n int) {
	var PlaslistTemp lagu
	var longest int

	longest = SearchLongest(PlaylistDoc)

	for i := 0; i < PlaylistDoc.sum; i++ {
		PlaslistTemp = PlaylistDoc.database[i]
		if i == longest {
			fmt.Print("*", PlaslistTemp.title, " ", PlaslistTemp.duration.minute, " menit ", PlaslistTemp.duration.second, " detik\n")
		} else {
			fmt.Print(PlaslistTemp.title, "\n")
		}
	}
}

func SearchLongest(PlaylistDoc playlist) int {
	var tsm, thisduration, longest int
	var PlaslistTemp lagu
	PlaslistTemp = PlaylistDoc.database[0]

	tsm = 0
	longest = 0

	for i := 1; i < PlaylistDoc.sum; i++ {
		PlaslistTemp = PlaylistDoc.database[i]
		thisduration = (PlaslistTemp.duration.minute * 60) + PlaslistTemp.duration.second
		if longest < thisduration {
			tsm = i
			longest = thisduration
		}
	}

	return tsm
}

func main() {
	var PlaylistDoc playlist
	PlaylistDoc.sum = 0
	buatPlaylist(&PlaylistDoc, &PlaylistDoc.sum)
	cetakPlaylist(PlaylistDoc, PlaylistDoc.sum)
}
