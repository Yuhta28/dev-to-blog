import os


val = input("Enter the name of the template: ")

# テンプレートディレクトリ作成
path = "./blog-posts/template-blog"
path_code = "./blog-posts/template-blog/code"
path_assets = "./blog-posts/template-blog/assets"

os.makedirs(path)
os.makedirs(path_code)
os.makedirs(path_assets)

# .gitkeepファイル作成
code_gitkeep = "./blog-posts/template-blog/code/.gitkeep"
assets_gitkeep = "./blog-posts/template-blog/assets/.gitkeep"

f = open(code_gitkeep, "w")
f.write("")
f.close()

f2 = open(assets_gitkeep, "w")
f2.write("")
f2.close()