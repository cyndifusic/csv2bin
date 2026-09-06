# csv2bin

## what is this

ok so the 2006 video game wii play for the wii has these ".bin" files in it that are literally just tables of numbers. for the games that are more "level-based" these numbers are used as basic parameters for those levels. easy examples include the number of miis in each level of find mii and the increasing speed of the ball on each rally in table tennis. that stuff is just plainly stored as numbers in one of those files. this is great news for aspiring modders because changing them requires zero programming.

the tricky part is that these numbers are stored in raw binary structures. you dont just get to type them into a spreadsheet you need to open a hex editor and cry. now really it's not that crazy, but you do need to worry about endianness, keep track of signed/unsigned integer/float types for each value, and most annoyingly, keep track of which parameter you're actually editing even though none of it's labeled. this makes trial-and-error testing considerably more tedious than it already is, and believe me, it already is.

to step around this at nintendo when they were making this game, they wrote a computer program called ExcelBin that made it so you DO just get to type them into a spreadsheet. thats what my program does too. you give it a .bin, it spits out a .csv, you open it with excel or google sheets or whatever and you get a labeled spreadsheet, you change what you wanna change, and then you can convert that the other direction into the modded .bin you'll then put into the game.

## how do i download

click the scary "code" button up at the top and download all the source code. this is because its python. so youre also going to need to install python. its easy i promise

## how do i use

1. open "switcher.py" in a text editor and change the number at the top to choose which file you want to target
2. go get that file from the wii play filesystem (see below) and copy it into the csv2bin folder, adding "_input" to the end of the filename
3. run bin2csv.py
4. copy and paste the resulting "..._output.csv" file and change "output" to "input". likewise, copy and paste the .bin and change "input" to "output".
5. open "..._input.csv" and change values
6. run csv2bin.py
7. "..._output.bin" should now be overwritten with your new values

## what is this "wii play filesystem" you speak of

if all you wanna do is browse the files and you already have a wii play .iso/.wbfs its actually pretty trivial. you just need to extract the files with debug features enabled in [dolphin] (look up "dolphin emulator extract filesystem" or something like that) and throw the resulting .carc archives into a program called [brawlcrate] so you can see whats in them.

putting those files back into the game requires a wii homebrew app called [riivolution] and im not going to explain that in this readme but i think the first video in [bigkitty's tanks modding tutorial series] describes the process

## how much of the game does this encompass

**fully implemented:**

- Find Mii 1P (wanted_1p_leveltable.bin)
- Find Mii 2P (wanted_2p_leveltable.bin)
- Table Tennis (leveltable.bin)
- Table Tennis (rallyleveluptable.bin)

**implemented with some parameters that are unknown or need more of an explanation:**

- Shooting Range (DucBalloonParam.bin)
- Shooting Range (DucCircleMatoParam.bin)
- Shooting Range (DucClayParam.bin)
- Shooting Range (DucDuckParam.bin)
- Shooting Range (DucUFOParam.bin)
- Pose Mii (BomQuestionParam.bin)

**not implemented because the file structure isn't documented and i don't have time:**

- Shooting Range (DucCanParam.bin)

this is all subject to change in new versions
for tanks files use [blitzkrieg tools]

## ai disclosure

i wrote this with my bare hands


