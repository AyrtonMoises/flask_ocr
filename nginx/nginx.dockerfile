FROM nginx:1.21-alpine
COPY /nginx/config/ /etc/nginx/
EXPOSE 80 443
ENTRYPOINT ["nginx"]

CMD ["-g", "daemon off;"]