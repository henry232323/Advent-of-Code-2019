import itertools
import collections
import asyncio

f = open("input.txt")
tpos = collections.defaultdict(int)
tpos.update(enumerate([int(x.strip()) for x in f.read().split(",")]))


def run_program():
    # print("starting new!")
    rbase = 0
    pos = tpos.copy()
    i = 0
    while True:
        inst = pos[i] % 100

        cmode = pos[i] // 100 % 10
        bmode = pos[i] // 1000 % 10
        amode = pos[i] // 10000 % 10

        if inst == 99:
            break
        if True or inst in (1, 2, 4, 5, 6, 7, 8, 9):
            if cmode == 0:
                cpos = pos[i + 1]
            elif cmode == 1:
                cpos = i + 1
            else:
                cpos = rbase + pos[i + 1]
            cval = pos[cpos]

            if bmode == 0:
                bpos = pos[i + 2]
            elif bmode == 1:
                bpos = i + 2
            else:
                bpos = rbase + pos[i + 2]
            bval = pos[bpos]

            if amode == 0:
                apos = pos[i + 3]
            elif amode == 1:
                apos = i + 3
            else:
                apos = rbase + pos[i + 3]
            aval = pos[apos]

        if inst == 1:
            # print(f"set pos {i + 3} to {cval} + {bval} = {cval + bval}")
            pos[apos] = cval + bval
            i += 4
        elif inst == 2:
            # print(f"set pos {i + 3} to {cval} * {bval} = {cval * bval}")
            pos[apos] = cval * bval
            i += 4
        elif inst == 3:
            pos[cpos] = int(input())  # int(await inq.get())
            # print(f"set pos {pos[i + 1]} to {pos[pos[i + 1]]}")
            i += 2
        elif inst == 4:
            print(cval)
            # await outq.put(pos[pos[i + 1]])
            i += 2
        elif inst == 5:
            if cval != 0:
                i = bval
            else:
                i += 3
        elif inst == 6:
            if cval == 0:
                i = bval
            else:
                i += 3
        elif inst == 7:
            pos[apos] = cval < bval
            i += 4
        elif inst == 8:
            pos[apos] = cval == bval
            i += 4
        elif inst == 9:
            rbase += cval
            i += 2
        else:
            raise ValueError("Invalid instruction: " + str(inst))

#inq = asyncio.Queue()
#inq.put_nowait(1)
#outq = asyncio.Queue()

#asyncio.run(run_program(inq, outq))
run_program()