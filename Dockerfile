# meminjam os yang sudah ada python
FROM python:3.9-slim 

# membuat user baru dengan nama user dan uid 1000
RUN useradd -m -u 1000 user
# set folder project nanti dalam container adalah /app
WORKDIR /app

# menyalin file di laptop kedalam container
COPY --chown=user . .
# Install dependencies
RUN pip install -r requirements.txt

# untuk memastikan container mengekspos port 7860
EXPOSE 7860

# Saat container dijalankan, jalankan perintah ini
CMD ["python", "app.py"]