
message.attach(MIMEText(message_body, "plain"))

        # Connect to Gmail SMTP
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        server.login(sender_email, sender_password)

        server.sendmail(sender_email, recipient_email, message.as_string())

        server.quit()

        return True

    except smtplib.SMTPRecipientsRefused:
        print("Invalid email address")
        return False

    except Exception as e:
        print("Email sending failed:", e)
        return False