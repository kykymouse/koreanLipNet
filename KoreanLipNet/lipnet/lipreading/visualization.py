import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects
import matplotlib.font_manager as fm

path ='../../../../usr/share/fonts/truetype/nanum/NanumMyeongjo.ttf'
fontprop = fm.FontProperties(fname=path, size=18)

def show_video_subtitle(frames, subtitle):
    fig, ax = plt.subplots()
    fig.show()

    plt.rcParams["font.family"] = 'NanumMyeongjo'

    print "++++++++++++++++++++++++++"
    print subtitle
    print "++++++++++++++++++++++++++"

    text = plt.text(0.5, 0.1, "", 
        ha='center', va='center', transform=ax.transAxes, 
        fontdict={'fontsize': 15, 'color':'white', 'fontweight': 500})
    text.set_path_effects([path_effects.Stroke(linewidth=3, foreground='black'),
        path_effects.Normal()])

    subs = subtitle.split()
    inc = max(len(frames)/(len(subs)+1), 0.01)

    i = 0
    img = None
    for frame in frames:
        sub = " ".join(subs[:int(i/inc)])
        # print frame
        print str(i) + " : " + sub
        # print sub
        text.set_text(sub)

        if img is None:
            img = plt.imshow(frame)
        else:
            img.set_data(frame)
        fig.canvas.draw()
        i += 1