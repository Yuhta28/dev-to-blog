import os


val = input("Enter the name of the template: ")

# テンプレートディレクトリ作成
path = "./blog-posts/" + val
path_code = "./blog-posts/" + val + "/code"
path_assets = "./blog-posts/" + val + "/assets"

os.makedirs(path)
os.makedirs(path_code)
os.makedirs(path_assets)

# .gitkeepファイル作成
code_gitkeep = "./blog-posts/" + val + "/code/.gitkeep"
assets_gitkeep = "./blog-posts/" + val + "/assets/.gitkeep"

f = open(code_gitkeep, "w")
f.write("")
f.close()

f2 = open(assets_gitkeep, "w")
f2.write("")
f2.close()

# 記事markdownファイル作成
blog = "./blog-posts/" + val + "/" + val + ".md"

f3 = open(blog, "w")
f3.write("")
f3.close()
