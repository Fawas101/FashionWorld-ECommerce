from django.shortcuts import render,redirect
from django.contrib import messages
from category.models import Category,Product
from admin_panel.forms import CategoryUpdateForm, ProductUpdateForm
from account.models import Account,UserProfile

# Create your views here.

def admin_home(request):
    return render(request,'admin/home.html') 

def admin_user(request):
    users = Account.objects.all().order_by("id")

    context = {"users": users}
    return render(request,'admin/user.html', context) 

def blockuser(request, id):
    user_to_block = Account.objects.get(id=id)

    if user_to_block.is_superadmin:
        messages.error(request, "Cannot block super admin.")
    elif user_to_block.is_staff and user_to_block == request.user:
        messages.error(request, "Cannot block yourself.")
    else:
        if user_to_block.is_blocked:
            user_to_block.is_blocked = False
            messages.success(request, f"{user_to_block.get_full_name()} has been unblocked.")
            user_to_block.save()
        else:
            user_to_block.is_blocked = True
            messages.success(request, f"{user_to_block.get_full_name()} has been blocked.")
            user_to_block.save()

    return redirect("admin_user")

def toggle_admin(request, id):
    user_to_toggle = Account.objects.get(id=id)

    # Super admin cannot toggle own admin status
    if user_to_toggle == request.user:
        messages.error(request, "Cannot change your own admin status.")
    else:
        user_to_toggle.is_staff = not user_to_toggle.is_staff
        user_to_toggle.save()

        action = "added" if user_to_toggle.is_staff else "removed"
        messages.success(request, f"{user_to_toggle.get_full_name()} has been {action} as an admin.")

    return redirect("usersprofile", id=user_to_toggle.id)

def usersprofile(request, id):
    u=Account.objects.get(pk=id)
    user = UserProfile.objects.get(user=u)
    context = {"user": user}
    return render(request, "admin_template/users_profile.html", context)


def admin_category(request):
    categories = Category.objects.all().order_by("id")

    context = {"categories": categories}
    return render(request,'admin/category.html', context) 

def add_Category(request):
    if request.method == "POST":
        form = CategoryUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category added successfully.')
            return redirect("admin_category")
    else:
        form = CategoryUpdateForm()

    context = {
        "form": form,
    }
    return render(request, "admin/categoryUpdate.html", context)

def edit_Category(request, slug):
    category = Category.objects.get(slug=slug)

    if request.method == "POST":
        print(request.POST)
        form = CategoryUpdateForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category edited successfully.')
            return redirect("admin_category")
    else:
        form = CategoryUpdateForm(instance=category)

    context = {
        "form": form,
    }
    return render(request, "admin/categoryUpdate.html", context)

def delete_Category(request, slug):
    category = Category.objects.get(slug=slug)
    category.delete()
    messages.success(request, 'Category deleted successfully.')
    return redirect("admin_category")


def admin_products(request):
    products = Product.objects.all().order_by("id")

    context = {"products": products}
    return render(request, "admin/products.html", context)


def add_Product(request):
    if request.method == "POST":
        form = ProductUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect("admin_products")
    else:
        form = ProductUpdateForm()

    context = {
        "form": form,
    }
    return render(request, "admin/productUpdate.html", context)


def edit_Product(request, id):
    product = Product.objects.get(id=id)

    if request.method == "POST":
        print(request.POST)
        form = ProductUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product edited successfully.')
            return redirect("admin_products")
    else:
        form = ProductUpdateForm(instance=product)

    context = {
        "form": form, 
    }
    return render(request, "admin/productUpdate.html", context)

def delete_Product(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    messages.success(request, 'Product deleted successfully.')
    return redirect("admin_products")



def admin_orders(request):
    return render(request,'admin/orders.html') 