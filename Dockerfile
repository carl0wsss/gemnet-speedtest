FROM adolfintel/speedtest:latest
COPY test_connexion.html /gemnet.html
COPY entrypoint.sh /custom_entrypoint.sh
RUN chmod +x /custom_entrypoint.sh
CMD ["/custom_entrypoint.sh"]
