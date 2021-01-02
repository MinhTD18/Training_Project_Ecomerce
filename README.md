# ECOMERCE

### Github
- clone source code
```
>> git clone <<https link or SSH key>>
```
- create new branch and switch to that branch
```
>> git branch <<branch name>> #create new branch
>> git checkout <<branch name>> #switch to specific branch, if 
you checkout a new brach, it will create a new branch and switch to that branch
```
- pull code and rebase
  (nho check xem minh dang o nhanh nao = git status)
```
>> git status <<branch name>> #kiem tra tinh trang nhanh va xem minh dang o nhanh nao
# Neu hien nhanh hien tai dang code chua xong thi dung >> git stash
# git stash se dua phan code chua xong ve mot bo nho tam
>> git checkout develops #switch to develops
>> git pull --rebase # update code hien tai cua nhanh develops
>> git checkout <<nhanh dang lam>>
>> git rebase develops #update code tu develops sang nhanh hien tai
(nho resolve confilct neu co)
>> git rebase --continue #sau khi resolve conflict thi tiep tuc rebase
>> git stash pop #day code dang code chua xong ra
```
- commit and push code
```
>> git commit -m "<<meassage>>" #commit your code to branch
>> git push #push your code to branch
```


#### git https: https://github.com/MinhTD18/Training_Project_Ecomerce.git

