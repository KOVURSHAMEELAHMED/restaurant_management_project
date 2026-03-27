def booking_confirmation(request):

    email = "customer@email.com"

    subject = "Hotel Booking Confirmation"

    message = """
    Dear Customer,

    Your hotel booking has been confirmed successfully.

    Thank you for choosing our hotel.

    Regards,
    Hotel Management
    """

    send_email(email, subject, message)

    return HttpResponse("Booking confirmed and email sent.")