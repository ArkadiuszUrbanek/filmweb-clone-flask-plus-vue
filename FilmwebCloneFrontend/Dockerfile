FROM node:current-alpine3.18

EXPOSE 5137

WORKDIR /filmweb-frontend-docker

COPY package.json ./
RUN npm install

COPY . .

CMD ["npm", "run", "dev"]