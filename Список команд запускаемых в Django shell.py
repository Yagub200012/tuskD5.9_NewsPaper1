#1 Создать двух пользователей.
a = User.objects.create_user('user1')
b = User.objects.create_user('user2')
#2 Создать два объекта модели Author, связанные с пользователями.
c = Author.objects.create(user_id = a)
d = Author.objects.create(user_id = b)

#3 Добавить 4 категории в модель Category.
e = Category.objects.create(categ_name = policy)
f = Category.objects.create(categ_name = crime)
g = Category.objects.create(categ_name = technologies)
h = Category.objects.create(categ_name = sport)

#4 Добавить 2 статьи и 1 новость
i = Post.objects.create(author_id = c, post_format = article, post_title = 'статья 1', post_text = 'текст статьи 1')
j = Post.objects.create(author_id = c, post_format = article, post_title = 'статья 2', post_text = 'текст статьи 2')
k = Post.objects.create(author_id = d, post_format = news, post_title = 'новость 1', post_text = 'текст новости 1')

#5 Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
l = PostCategory.objects.create(post_id = i, cathegory_id = e)
m = PostCategory.objects.create(post_id = i, cathegory_id = f)
n = PostCategory.objects.create(post_id = j, cathegory_id = g)
o = PostCategory.objects.create(post_id = j, cathegory_id = h)
p = PostCategory.objects.create(post_id = k, cathegory_id = e)
q = PostCategory.objects.create(post_id = k, cathegory_id = g)

#6 Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
r = Comment.objects.create(post_id = i, user_id = a, comm_text = 'текст комментария 1')
s = Comment.objects.create(post_id = i, user_id = b, comm_text = 'текст комментария 2')
t = Comment.objects.create(post_id = j, user_id = a, comm_text = 'текст комментария 3')
u = Comment.objects.create(post_id = k, user_id = b, comm_text = 'текст комментария 4')

#7 Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
i.like()
k.like()
k.like()
r.like()
t.like()
t.like()
u.like()

#8 Обновить рейтинги пользователей.
c.update_raiting()
d.update_raiting()

#9 Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
[Author.objects.all().order_by('-auth_rating').values('auth_rating')[0],Author.objects.all().order_by('-auth_rating')[0].user_id]

#10 Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
[Post.objects.all().order_by('-post_rating').values('post_datetime', 'post_rating', 'post_title')[0],Post.objects.all().order_by('-post_rating')[0].author_id.user_id, Post.objects.all().order_by('-post_rating')[0].preview()]

#11 Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
Comment.objects.filter(post_id = (Post.objects.all().order_by('-post_rating')[0])).values('comm_datetime', 'user_id', 'comm_rating', 'comm_text')




