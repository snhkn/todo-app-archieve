package com.github.snhkn.rest.webservices.todoAppwebservice.todo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.stereotype.Component;

@Component
public class TodoCommadLineRunner implements CommandLineRunner {

	@Autowired
	private TodoJpaRepository repository;

	@Override
	public void run(String... args) throws Exception {
		System.out.println(repository.findById(10002l).get().getDescription());

	}

}
