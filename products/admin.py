from django.contrib import admin
from products.models import ProductCategory, Product, Basket

# Register your models here.
admin.site.register(ProductCategory)
admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category') # какие поля будут отображаться в списке товаров в админке
    fields = ('name', 'image', ('description', 'short_description'), ('price', 'quantity'), 'category') # соединяем в админке поля, чтобы они не выводились наждый на новой строке
    # readonly_fields = ('price',) # какие поля доступны лишь для чтения
    ordering = ('name',) # все поля будут отфильтрованы в алфавитном порядке (А-Я). если сделать '-name', то будет (Я-А). можно фильтровать по любому параметру
    search_fields = ('name',) # создаёт поле для поиска по имени


class BasketAdminInline(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('product', 'created_timestamp',)
    extra = 0