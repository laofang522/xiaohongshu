#!/usr/bin/env python3
"""便签贴纸风封面生成器（AutoTuwen）
用法: python3 make_cover.py <底图.jpg> <输出.png> "第一行,第二行" "关键词行"
依赖: Pillow (pip install pillow)
"""
import sys, os
from PIL import Image, ImageDraw, ImageFont

def find_handwriting_font():
    candidates = [
        "/System/Library/AssetsV2/com_apple_MobileAsset_Font8/a3c69464b629577766c23bcdb12ffbfe3759b923.asset/AssetData/Hanzipen.ttc",
        "/System/Library/Fonts/Supplemental/Bradley Hand Bold.ttf",
        "/System/Library/Fonts/Supplemental/Chalkboard.ttc",
    ]
    for p in candidates:
        if os.path.exists(p): return p
    raise SystemExit("找不到手写字体，请在脚本里补充 FONT 路径")

def main():
    src, out, top_text, key_text = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    font_path = find_handwriting_font()
    img = Image.open(src).convert("RGBA")
    w, h = img.size
    tw, th = (int(h*3/4), h) if w*4 > h*3 else (w, int(w*4/3))
    img = img.crop(((w-tw)//2, (h-th)//2, (w-tw)//2+tw, (h-th)//2+th)).resize((1080,1440))

    lines = top_text.split(",")
    note = Image.new("RGBA", (900, 200 + 140*len(lines)), (0,0,0,0))
    nd = ImageDraw.Draw(note)
    nh = 200 + 140*len(lines)
    nd.rounded_rectangle([0,0,900,nh], radius=18, fill=(255,244,180,242))
    f1 = ImageFont.truetype(font_path, 58); f2 = ImageFont.truetype(font_path, 120)
    y = 45
    for line in lines:
        nd.text((50,y), line, font=f1, fill=(50,50,50)); y += 90
    nd.text((50,y+10), key_text, font=f2, fill=(200,50,40))
    nd.line([50, y+150, 50+f2.getlength(key_text), y+162], fill=(120,190,120), width=10)
    note = note.rotate(-5, expand=True, resample=Image.BICUBIC)
    img.paste(note, ((1080-note.width)//2, 1440-note.height-160), note)
    img.convert("RGB").save(out)
    print("saved:", out)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main()
