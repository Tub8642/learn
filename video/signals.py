from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ContactMessage
from .telegram_utils import send_telegram_message

post_save, sender=ContactMessage
def notify_about_new_message(sender, instance, created, **kwargs):
    if created:  # Отправляем уведомление только при создании, а не при обновлении
        message_text = (
            f"📩 <b>Новая заявка с сайта!</b>\n\n"
            f"👤 <b>Имя:</b> {instance.name}\n"
            f"📞 <b>Контакт:</b> {instance.contact_value} ({instance.contact_type})\n"
            f"💬 <b>Сообщение:</b> {instance.message or 'Не указано'}"
        )
        send_telegram_message(message_text)